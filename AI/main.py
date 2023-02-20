import numpy as np
from tensorflow import keras
from AI.dao.output_dao import OutputDAO


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
        raw_res = model.predict(x)
        answer = np.argmax(raw_res)
        digits, res = OutputDAO().get_processed_digit_output(raw_res)
        return digits, res, answer


if __name__ == '__main__':
    pass
