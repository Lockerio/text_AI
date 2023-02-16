import numpy as np
from keras.datasets import mnist         # Библиотека базы выборок Mnist
from tensorflow import keras
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D


class DigitNeuralNetwork:
    def __init__(self):
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        # стандартизация входных данных
        x_train = x_train / 255
        x_test = x_test / 255

        self.y_train_cat = keras.utils.to_categorical(y_train, 10)
        self.y_test_cat = keras.utils.to_categorical(y_test, 10)

        self.x_train = np.expand_dims(x_train, axis=3)
        self.x_test = np.expand_dims(x_test, axis=3)

        self.model = keras.Sequential([
            Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2), strides=2),
            Conv2D(64, (3, 3), padding='same', activation='relu'),
            MaxPooling2D((2, 2), strides=2),
            Flatten(),
            Dense(128, activation='relu'),
            Dense(10, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def __repr__(self):
        return repr(self.model.summary())

    def train_network(self):
        self.model.fit(self.x_train, self.y_train_cat, batch_size=32, epochs=5, validation_split=0.2)

    def check_network(self):
        self.model.evaluate(self.x_test, self.y_test_cat)

    def save_network_model(self, model_path):
        self.model.save(model_path)
        print("Модель сохранена")


if __name__ == '__main__':
    nn = DigitNeuralNetwork()
    nn.train_network()
    nn.check_network()
    nn.save_network_model("digit_recognition_model")
