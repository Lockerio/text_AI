import os
import numpy as np
from PIL import Image


class PrepareDataDAO:
    """
    Prepare data for network letter dataset.
    """
    def prepare_cyrillic(self, directory):
        """
        Handle directory with raw images of cyrillic symbols.
        :param directory: Path to images.
        """
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = root + "/" + file
                self.make_background(filepath)
                self.resize_img_to_28_28(filepath)
                self.change_black_to_white(filepath)
            print(f"Directory '{root}' processed.")

    @staticmethod
    def make_background(filepath):
        """
        Fill background with white color. If we didn't fill background,
        we would get absolutely black image, because there are symbols, colored with black in source files.
        :param filepath: Directory with images.
        """
        img = Image.open(filepath)
        fill_color = (255, 255, 255)
        img = img.convert("RGBA")
        if img.mode in ('RGBA', 'LA'):
            background = Image.new(img.mode[:-1], img.size, fill_color)
            background.paste(img, img.split()[-1])
            img = background

        img.convert("RGB").save(filepath)

    @staticmethod
    def resize_img_to_28_28(filepath):
        """
        Resize images to fit (28 * 28, like in the MNIST).
        :param filepath: Directory with images.
        """
        img = Image.open(filepath)
        img = img.resize((28, 28))
        img.save(filepath)

    @staticmethod
    def change_black_to_white(filepath):
        """
        Change background color to black and symbol color to white.
        Neural network recognize symbols by white pixels
        :param filepath: Directory with images.
        """
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
    PrepareDataDAO().prepare_cyrillic("../data/cyrillic/")
