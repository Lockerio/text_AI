from tensorflow import keras
from AI.utils.work_with_images import WorkerWithImages
import matplotlib.pyplot as plt
import numpy as np


def set_network_model(network_name):
    model_path = f"{network_name}/{network_name}_model"
    try:
        user_model = keras.models.load_model(model_path)
        return user_model

    except OSError:
        print(f"Файл {model_path} не найден! Возможна ошибка в написании нейросети")


if __name__ == '__main__': 
    model = set_network_model("digit_recognition")
    img = WorkerWithImages().convert_28_28_image_to_pixels_array("resources/adin.png")

    x = np.expand_dims(img, axis=0)
    res = model.predict(x)
    print(res)
    print(np.argmax(res))

    plt.imshow(img, cmap=plt.cm.binary)
    plt.show()
