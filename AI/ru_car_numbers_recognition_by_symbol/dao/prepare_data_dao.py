import os
import numpy as np
from PIL import Image


class PrepareDataDAO:
    def prepare_cyrillic(self, directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = root + "/" + file

                self.make_background(filepath)
                self.resize_img_to_28_28(filepath)
                self.change_black_to_white(filepath)
            print(f"Directory '{root}' processed.")

    @staticmethod
    def make_background(filepath):
        img = Image.open(filepath)
        fill_color = (255, 255, 255)  # your new background color
        img = img.convert("RGBA")  # it had mode P after DL it from OP
        if img.mode in ('RGBA', 'LA'):
            background = Image.new(img.mode[:-1], img.size, fill_color)
            background.paste(img, img.split()[-1])  # omit transparency
            img = background

        img.convert("RGB").save(filepath)

    @staticmethod
    def resize_img_to_28_28(filepath):
        img = Image.open(filepath)
        img = img.resize((28, 28))
        img.save(filepath)

    @staticmethod
    def change_black_to_white(filepath):
        img = Image.open(filepath)
        img = np.array(img)
        raw_pixels = np.asarray(img, float)

        pixels = np.array([
            [
                pixel[0] / 255 for pixel in row
            ]
            for row in raw_pixels
        ])

        pixels = pixels * (-1) + 1
        img = Image.fromarray(np.uint8(pixels * 255))
        img.save(filepath)


if __name__ == '__main__':
    PrepareDataDAO().prepare_cyrillic("../data/cyrillic/I")
