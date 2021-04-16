from io import BytesIO
from typing import DefaultDict, List, Set, Tuple

from PIL import Image, ImageDraw

from codenames.duet.game import GameMixin, Team, Identity, BOARD_SIZE
from codenames.resources.fonts import FontList, PT_SANS, DEJA_VU_SANS
from codenames.resources.images import BOARD, ASSASSIN, CHECKMARK_TOKEN
from codenames.resources.images import ASSASSIN_MARK, DUET_AGENT_MARK
from codenames.resources.images import DUET_AGENT_CARDS, BYSTANDER_TOKENS

BOARD_COLUMN_COUNT = 5


def hor_shift(pos: int) -> int:
    return 202 * (pos // BOARD_COLUMN_COUNT)

def vert_shift(pos: int) -> int:
    return 133 * (pos % BOARD_COLUMN_COUNT)


def draw_text_centered(draw: ImageDraw.Draw, xy: Tuple[int, int], text: str, face: FontList):
    x, y = xy

    for font in face:
        width, _ = draw.textsize(text, font)
        if width <= 150:
            draw.text((x - width // 2, y - int(font.size / 1.7) + 1), text, font=font, fill="black")
            return


def render_board(board: GameMixin, for_team: Team) -> BytesIO:
    board_image = BOARD.copy()
    draw = ImageDraw.Draw(board_image)

    face = PT_SANS if board.wordlist_code in range(6) else DEJA_VU_SANS

    for pos in range(BOARD_SIZE):
        draw_text_centered(
            draw,
            (116 + hor_shift(pos), 104 + vert_shift(pos)),
            board.words[pos].upper(),
            face
        )

        identity = board.get_identity(pos, for_team.opposed())
        if identity == Identity.AGENT:
            board_image.alpha_composite(DUET_AGENT_MARK, (17 + hor_shift(pos), 17 + vert_shift(pos)))
        elif identity == Identity.ASSASSIN:
            board_image.alpha_composite(ASSASSIN_MARK, (17 + hor_shift(pos), 17 + vert_shift(pos)))

    guesses: DefaultDict[Identity, List[Tuple[int, Team]]] = DefaultDict(list)

    for pos, team, identity in board.get_guess_history():
        guesses[identity].append((pos, team))

    for i, (pos, team) in enumerate(guesses[Identity.AGENT]):
        img = DUET_AGENT_CARDS[i]
        if team != for_team:
            img = img.transpose(Image.ROTATE_180)

        board_image.alpha_composite(img, (21 + hor_shift(pos), 21 + vert_shift(pos)))

    for pos, team in guesses[Identity.ASSASSIN]:
        img = ASSASSIN
        if team != for_team:
            img = img.transpose(Image.ROTATE_180)

        board_image.alpha_composite(img, (21 + hor_shift(pos), 21 + vert_shift(pos)))

    bystander_positions: Set[int] = set()
    for i, (pos, team) in enumerate(guesses[Identity.BYSTANDER]):
        img = BYSTANDER_TOKENS[i]
        if team != for_team:
            img = img.transpose(Image.ROTATE_180)

        x, y = 143 + hor_shift(pos), 24 + vert_shift(pos)
        if pos in bystander_positions:
            x -= 69
        else:
            bystander_positions.add(pos)

        board_image.alpha_composite(img, (x, y))

    placed_bystander_token_count = len(guesses[Identity.BYSTANDER])
    for i in range(board.free_token_count):
        img = BYSTANDER_TOKENS[i + placed_bystander_token_count]

        board_image.alpha_composite(img, (32 + 71 * i, 686))

    for i in range(board.total_token_count - placed_bystander_token_count - board.free_token_count):
        board_image.alpha_composite(CHECKMARK_TOKEN, (943 - 71 * i, 686))

    result = BytesIO()
    result.name = "board.png"
    board_image.save(result, "PNG")
    result.seek(0)

    return result
