class OutputDAO:
    @staticmethod
    def get_processed_digit_output(raw_output):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        raw_output = raw_output[0]
        output = dict(zip(digits, raw_output))
        return output

    @staticmethod
    def get_processed_digits_letters_output(raw_output, answer):
        letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "А", "Б", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        answer_dict = dict(zip(digits, letters))
        answer = answer_dict[answer]
        raw_output = raw_output[0]
        output = dict(zip(letters, raw_output))
        print(output)
        print(answer)
        return output, answer


if __name__ == '__main__':
    pass
