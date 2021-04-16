from typing import List

from PIL import ImageFont


FontList = List[ImageFont.ImageFont]


PT_SANS: FontList = [
    ImageFont.truetype("resources/PTSansCaptionBold.ttf", size)
    for size in range(25, 11, -1)
]


DEJA_VU_SANS: FontList = [
    ImageFont.truetype("resources/DejaVuSans-Bold.ttf", size)
    for size in range(25, 11, -1)
]
