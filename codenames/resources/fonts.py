from typing import List

from PIL import ImageFont


FontList = List[ImageFont.ImageFont]


PT_SANS: FontList = [
    ImageFont.truetype("resources/PTSansCaptionBold.ttf", size)
    for size in range(25, 11, -1)
]


FARSI_WEB_TERAFIK: FontList = [
    ImageFont.truetype("resources/FarsiWebTerafikBold.ttf", size)
    for size in range(25, 11, -1)
]
