class OutputDAO:
    @staticmethod
    def get_processed_digit_output(raw_output):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        output = raw_output[0]
        return digits, output


if __name__ == '__main__':
    pass
