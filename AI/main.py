from tensorflow import keras
import numpy as np


def recognize_user_input(network_name, pixels):
    model_path = f"AI/{network_name}/{network_name}_model"

    if __name__ == '__main__':
        model_path = f"{network_name}/{network_name}_model"

    try:
        model = keras.models.load_model(model_path)

    except OSError:
        print(f"Файл {model_path} не найден! Возможна ошибка в написании названия нейросети")

    else:
        x = np.expand_dims(pixels, axis=0)
        res = model.predict(x)
        answer = np.argmax(res)

        return res, answer


if __name__ == '__main__':
    pass
