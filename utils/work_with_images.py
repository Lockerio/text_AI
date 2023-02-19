import base64
import numpy as np
from PIL import Image
from io import BytesIO


class WorkerWithImages:
    @staticmethod
    def open_image(raw_img):
        if type(raw_img) == str:
            img = raw_img.split(',')[1]
            img = Image.open(BytesIO(base64.b64decode(img)))
        else:
            img = Image.open(raw_img)
        return img

    @staticmethod
    def assert_image(img):
        required_size = (28, 28)

        if img.size != required_size:
            img = img.resize((28, 28))
        return img

    def convert_28_28_image_to_pixels_array(self, raw_img):
        raw_img = self.open_image(raw_img)
        img = self.assert_image(raw_img)
        img = np.array(img)
        raw_pixels = np.asarray(img, float)

        pixels = np.array([
            [
                pixel[0] / 255 for pixel in row
            ]
            for row in raw_pixels
        ])
        return pixels

    @staticmethod
    def change_black_to_white(raw_pixels):
        pixels = raw_pixels * (-1) + 1
        return pixels


if __name__ == '__main__':
    pass
