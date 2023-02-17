import cv2
import numpy as np
from PIL import Image


class WorkerWithImages:
    def convert_28_28_image_to_pixels_array(self, image_path):
        self.assert_image_size(image_path)
        img = cv2.imread(image_path)
        raw_pixels = np.asarray(img, float)

        pixels = [
            [
                pixel[0] / 255 for pixel in row
            ]
            for row in raw_pixels
        ]
        return pixels

    @staticmethod
    def assert_image_size(image_path):
        img = Image.open(image_path)
        required_size = (28, 28)

        if img.size != required_size:
            new_image = img.resize((28, 28))
            new_image.save(image_path)


if __name__ == '__main__':
    pass
