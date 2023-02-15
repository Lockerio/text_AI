import os
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist         # Библиотека базы выборок Mnist
from tensorflow import keras
from keras.layers import Dense, Flatten
from AI.utils import WorkerWithImages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class NeuralNetwork:
    @staticmethod
    def create_network():
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        # стандартизация входных данных
        x_train = x_train / 255
        x_test = x_test / 255

        y_train_cat = keras.utils.to_categorical(y_train, 10)
        y_test_cat = keras.utils.to_categorical(y_test, 10)



        model = keras.Sequential([
            Flatten(input_shape=(28, 28, 1)),
            Dense(128, activation='relu'),
            Dense(10, activation='softmax')
        ])

        print(model.summary())      # вывод структуры НС в консоль

        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)

        model.evaluate(x_test, y_test_cat)

        n = 1
        x = np.expand_dims(x_test[n], axis=0)
        res = model.predict(x)
        print(res)
        print(np.argmax(res))

        plt.imshow(x_test[n], cmap=plt.cm.binary)
        plt.show()

        # Распознавание всей тестовой выборки
        pred = model.predict(x_test)
        pred = np.argmax(pred, axis=1)

        print(pred.shape)

        print(pred[:20])
        print(y_test[:20])

        # Выделение неверных вариантов
        mask = pred == y_test
        print(mask[:10])

        x_false = x_test[~mask]
        y_false = x_test[~mask]

        print(x_false.shape)

        # Вывод первых 25 неверных результатов
        plt.figure(figsize=(10, 5))
        for i in range(25):
            plt.subplot(5, 5, i+1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(x_false[i], cmap=plt.cm.binary)

        plt.show()

        model.save("digit_recognition_model")

        # отображение первых 25 изображений из обучающей выборки
        plt.figure(figsize=(10, 5))
        for i in range(25):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(x_train[i], cmap=plt.cm.binary)
        plt.show()


def do_main():
    # create_network()
    model = keras.models.load_model("digit_recognition_model")

    img = WorkerWithImages().convert_28_28_image_to_numpy_array("../resources/dva.png")

    x = np.expand_dims(img, axis=0)
    res = model.predict(x)
    print(res)
    print(np.argmax(res))
    plt.imshow(img, cmap=plt.cm.binary)
    plt.show()


if __name__ == '__main__': 
    do_main()
