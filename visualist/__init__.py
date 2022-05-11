from PIL import Image, ImageDraw, ImageFont
import os
from typing import List


class Visualist:
    def __init__(self, image_size=None, cell_size=64, space=32):

        self.CELL_SIZE = cell_size
        self.SPACE = space

        font_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fonts", "Roboto-Medium.ttf"
        )
        self.font = ImageFont.truetype(font_path, int(self.CELL_SIZE / 2))

    def img_from_list(
        self,
        L,
        highlight_indexes=[],
        image_size=None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
        matrix=False
    ) -> Image:

        start_of_drawing = (len(L) / 2) * (self.CELL_SIZE + self.SPACE)
        if image_size:
            IMAGE_SIZE = image_size
        elif matrix:
            IMAGE_SIZE = (int(2 * start_of_drawing), int(self.CELL_SIZE + self.SPACE))
        else:
            IMAGE_SIZE = (int(2 * start_of_drawing), int(3 * self.CELL_SIZE))

        img = Image.new("RGBA", IMAGE_SIZE, (255, 255, 255, 255))

        MIDDLE = (img.size[0] / 2, img.size[1] / 2)

        draw = ImageDraw.Draw(img)
        pointer = MIDDLE[0] - start_of_drawing + self.SPACE / 2

        for index, item in enumerate(L):
            X0 = pointer
            X1 = pointer + self.CELL_SIZE

            rect_color = color
            if index in highlight_indexes:
                rect_color = highlight_color
            draw.rectangle(
                [
                    (X0, MIDDLE[1] - self.CELL_SIZE / 2),
                    (X1, MIDDLE[1] + self.CELL_SIZE / 2),
                ],
                fill=rect_color,
            )

            text_size = draw.textsize(str(item), font=self.font)
            draw.text(
                (
                    pointer + self.CELL_SIZE / 2 - text_size[0] / 2,
                    MIDDLE[1] - self.CELL_SIZE / 2 + text_size[1] / 2,
                ),
                str(item),
                font=self.font,
            )

            if show_indexes:
                text_size = draw.textsize(str(index), font=self.font)
                draw.text(
                    (
                        pointer + self.CELL_SIZE / 2 - text_size[0] / 2,
                        MIDDLE[1]
                        - self.CELL_SIZE
                        - self.CELL_SIZE / 2
                        + text_size[1] / 2,
                    ),
                    str(index),
                    font=self.font,
                    fill=(0, 0, 0, 255),
                )

            pointer += self.CELL_SIZE + self.SPACE

        return img

    def img_from_lists(
        self,
        L,
        highlight_indexes,
        image_size=None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
    ) -> Image:
        imgs = []
        sum_height = 0
        max_width = 0
        for l, hi in zip(L, highlight_indexes):
            if image_size is not None:
                img = self.img_from_list(
                    l,
                    hi,
                    (image_size[0], int(image_size[1] / len(L))),
                    color,
                    highlight_color,
                    show_indexes,
                )
            else:
                img = self.img_from_list(
                    l, hi, image_size, color, highlight_color, show_indexes
                )
            max_width = max(max_width, img.size[0])
            sum_height += img.size[1]
            imgs.append(img)

        final_img = Image.new("RGBA", (max_width, sum_height), (255, 255, 255, 255))

        for index, img in enumerate(imgs):
            final_img.paste(
                img, (int(max_width / 2 - img.size[0] / 2), index * img.size[1])
            )

        return final_img

    def img_from_matrix(
        self,
        L,
        HI,
        image_size=None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
    ) -> Image:
        imgs = []
        sum_height = 0
        max_width = 0        
        for l, hi in zip(L, HI):
            if image_size is not None:
                img = self.img_from_list(
                    l,
                    hi,
                    (image_size[0], int(image_size[1] / len(L))),
                    color,
                    highlight_color,
                    False,
                    True
                )
            else:
                img = self.img_from_list(
                    l, hi, image_size, color, highlight_color, False, True
                )
                
            max_width = max(max_width, img.size[0])
            sum_height += img.size[1]
            imgs.append(img)

        final_img = Image.new("RGBA", (max_width, sum_height), (255, 255, 255, 255))

        for index, img in enumerate(imgs):
            final_img.paste(
                img, (int(max_width / 2 - img.size[0] / 2), index * img.size[1])
            )

        return final_img