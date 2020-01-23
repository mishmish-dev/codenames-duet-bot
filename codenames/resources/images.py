import os.path
from typing import List

from PIL import Image


def load_image(path: str) -> Image.Image:
    image = Image.open(path)
    image.load()
    return image

def load_images_from_directory(path: str) -> List[Image.Image]:
    return [
        load_image(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(path)
        for filename in sorted(filenames)
    ]


BOARD = load_image("resources/images/common/board.png")
ASSASSIN = load_image("resources/images/common/assassin.png")
CHECKMARK_TOKEN = load_image("resources/images/duet/checkmark_token.png")
ASSASSIN_MARK = load_image("resources/images/common/assassin_mark.png")
DUET_AGENT_MARK = load_image("resources/images/duet/agent_mark.png")

DUET_AGENT_CARDS = load_images_from_directory("resources/images/duet/agent_cards")
BYSTANDER_TOKENS = (
    load_images_from_directory("resources/images/duet/bystander_tokens")
    + load_images_from_directory("resources/images/duet/bystander_extra_tokens")
)
