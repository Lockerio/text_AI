import base64
import numpy as np
from PIL import Image
from io import BytesIO


class WorkerWithImages:
    @staticmethod
    def open_image(raw_img):
        """
        Open different types of images.
        :param raw_img: Painted or uploaded user image from site.
        :return: Opened PIL image.
        """
        if type(raw_img) is str:
            img = raw_img.split(',')[1]
            img = Image.open(BytesIO(base64.b64decode(img)))
        else:
            img = Image.open(raw_img)
        return img

    def convert_image_to_base(self, img):
        """
        Convert PIL image or image's base string to source base string for HTML.
        :param img: Input image.
        :return: Image base string.
        """
        if type(img) is not str:
            img = self.open_image(img)
            buffered = BytesIO()
            img.save(buffered, format=img.format)
            image_data = base64.b64encode(buffered.getvalue()).decode("utf-8")
            image_data = "data:image/;base64data:" + image_data
        else:
            image_data = "data:image/;base64" + img
        return image_data

    @staticmethod
    def assert_image(img):
        """
        Check and resize inputted image.
        :param img: Inputted image.
        :return: Verified picture.
        """
        required_size = (28, 28)
        if img.size != required_size:
            img = img.resize((28, 28))
        return img

    def convert_28_28_image_to_pixels_array(self, raw_img):
        """
        Convert image to numpy array.
        :param raw_img: Inputted image.
        :return: Array of pixels.
        """
        raw_img = self.open_image(raw_img)
        img = self.assert_image(raw_img)
        img = np.array(img)
        raw_pixels = np.asarray(img, float)

        pixels = np.array([
            [
                # Standardization of data.
                pixel[0] / 255  for pixel in row
            ]
            for row in raw_pixels
        ])
        return pixels

    @staticmethod
    def change_black_to_white(raw_pixels):
        """
        Change background color to black and symbol color to white.
        Neural network recognize symbols by white pixels
        :param raw_pixels: Array of pixels.
        :return: Verified picture.
        """
        pixels = raw_pixels * (-1) + 1
        return pixels


if __name__ == '__main__':
    pass
