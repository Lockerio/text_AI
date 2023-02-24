import os
from PIL import Image


class UploadDatasetsDAO:
    """
    Uploading datasets by prepared data.
    """
    def __init__(self):
        self.max_amount_training_files = 380
        self.max_amount_testing_files = 500  # For digits. Too much files for my network in source folder.

    def upload_cyrillic(self, directory):
        for root, dirs, files in os.walk(directory):
            files_counter = 0
            for file in files:
                source_filepath = root + "/" + file
                files_counter += 1
                img = Image.open(source_filepath)

                if files_counter <= self.max_amount_training_files:
                    path = f"../datasets/training/{self.get_symbol(root)}/{file}"
                    img.save(path)
                else:
                    path = f"../datasets/testing/{self.get_symbol(root)}/{file}"
                    img.save(path)
            print(f"Directory '{root}' processed.")

    def upload_digits(self, directory):
        for root, dirs, files in os.walk(directory):
            files_counter = 0
            for file in files:
                source_filepath = root + "/" + file
                files_counter += 1
                img = Image.open(source_filepath)

                if files_counter <= self.max_amount_training_files:
                    path = f"../datasets/training/{self.get_symbol(root)}/{file}"
                    img.save(path)
                elif files_counter <= self.max_amount_testing_files:
                    path = f"../datasets/testing/{self.get_symbol(root)}/{file}"
                    img.save(path)
                else:
                    break

            print(f"Directory '{root}' processed.")

    @staticmethod
    def get_symbol(source_filepath):
        letter = source_filepath.split("/")[-1]
        return letter


if __name__ == '__main__':
    UploadDatasetsDAO().upload_cyrillic("../data/cyrillic/")
    UploadDatasetsDAO().upload_digits("../data/digits/MNISTDatasetJPGformat/MNISTJPGtesting/")
