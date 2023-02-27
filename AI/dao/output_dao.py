class OutputDAO:
    """
    Allows you to make the output of the results visually better.
    """
    @staticmethod
    def get_processed_digit_output(raw_output):
        """
        Digits output.
        :param raw_output: Neural network output.
        :return: Dictionary of digits as keys and neural network output as values.
        """
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        raw_output = raw_output[0]
        output = dict(zip(digits, raw_output))
        return output

    @staticmethod
    def get_processed_letters_output(raw_output, answer):
        """
        Russian car numbers letters output.
        :param raw_output: Neural network output.
        :param answer: Neural network prediction.
        :return: Dictionary of letters and neural network output as values, neural network prediction.
        """
        letters = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        answer_dict = dict(zip(digits, letters))  # Match letters with indexes.
        answer = answer_dict[answer]
        raw_output = raw_output[0]
        output = dict(zip(letters, raw_output))
        return output, answer

    @staticmethod
    def get_processed_symbols_output(raw_output, answer):
        """
        Russian car numbers symbols output.
        :param raw_output: Neural network output.
        :param answer: Neural network prediction.
        :return: Dictionary of digits as keys and neural network output as values, neural network prediction.
        """
        letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        answer_dict = dict(zip(digits, letters))  # Match symbols with indexes.
        answer = answer_dict[answer]
        raw_output = raw_output[0]
        output = dict(zip(letters, raw_output))
        return output, answer


if __name__ == '__main__':
    pass
