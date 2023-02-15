import cv2
import numpy as np


class WorkerWithImages:
    @staticmethod
    def convert_28_28_image_to_numpy_array(image_path):
        img = cv2.imread(image_path)
        raw_pixels = np.asarray(img, float)

        pixels = [
            [
                pixel[0] / 255 for pixel in row
            ]
            for row in raw_pixels
        ]
        return pixels


def do_main():
    pass
    
    
if __name__ == '__main__': 
    do_main()
