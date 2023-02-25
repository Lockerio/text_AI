import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator


class DigitsLettersNeuralNetwork:
    """
    Create, train and test neural network for recognition russian car numbers.
    """
    def __init__(self):
        """
        Create network model.
        """
        self.size = 28, 28
        self.batch_size = 5
        self.epochs = 4
        training_data_dir = "datasets/training"
        testing_data_dir = "datasets/testing"

        training_data_gen = ImageDataGenerator(rescale=1/255)
        testing_data_gen = ImageDataGenerator(rescale=1 / 255)

        self.train_generator = training_data_gen.flow_from_directory(
            training_data_dir,
            color_mode='grayscale',
            target_size=self.size,
            batch_size=self.batch_size,
            class_mode='categorical'
        )
        self.test_generator = testing_data_gen.flow_from_directory(
            testing_data_dir,
            color_mode='grayscale',
            target_size=self.size,
            batch_size=self.batch_size,
            class_mode='categorical'
        )

        self.model = keras.Sequential([
            Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2), strides=2),
            Conv2D(64, (3, 3), padding='same', activation='relu'),
            MaxPooling2D((2, 2), strides=2),
            Flatten(),
            Dense(200, activation='relu'),
            Dense(self.train_generator.num_classes, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def __repr__(self):
        return repr(self.model.summary())

    def train_network(self):
        self.model.fit_generator(
            self.train_generator,
            steps_per_epoch=np.floor(self.train_generator.n/self.batch_size),
            epochs=self.epochs,
            validation_data=self.test_generator,
            validation_steps=np.floor(self.test_generator.n / self.batch_size)
        )

    def check_network(self):
        self.model.evaluate(self.test_generator)

    def save_network_model(self, model_path):
        self.model.save(model_path)
        print("Модель сохранена")


if __name__ == '__main__':
    nn = DigitsLettersNeuralNetwork()
    nn.train_network()
    nn.check_network()
    nn.save_network_model("ru_car_numbers_recognition_by_symbol_model")
