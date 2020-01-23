from typing import List

from PIL import ImageFont


FONTS: List[ImageFont.ImageFont] = [
    ImageFont.truetype("resources/PTSansCaptionBold.ttf", size)
    for size in range(25, 11, -1)
]
