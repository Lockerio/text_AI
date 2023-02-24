import numpy as np
from tensorflow import keras
from AI.dao.output_dao import OutputDAO


def recognize_user_input(network_name, pixels):
    """
    Predict answer to user input.
    :param network_name: Choosing a neural network.
    :param pixels: Handled user image.
    :return: Network prediction.
    """
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
        res, answer = OutputDAO().get_processed_symbols_output(raw_res, answer)
        return res, answer


if __name__ == '__main__':
    pass
