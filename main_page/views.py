from flask import render_template, Blueprint, request
from utils.work_with_images import WorkerWithImages
from AI.main import recognize_user_input
from main_page.dao.input_files_dao import InputFilesDAO


main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates', static_folder='../static')


@main_page_blueprint.route('/')
def return_main_page():
    return render_template('index.html', error="")


@main_page_blueprint.route('/results', methods=['POST'])
def return_results_page():
    img = request.files.get("picture")
    images_worker = WorkerWithImages()

    # file
    if img:
        pixels = images_worker.convert_28_28_image_to_pixels_array(img)

    # base
    else:
        img = request.form["picture"]
        raw_pixels = images_worker.convert_28_28_image_to_pixels_array(img)
        pixels = images_worker.change_black_to_white(raw_pixels)
        img = images_worker.convert_image_to_base(img)

    result, answer = recognize_user_input("digit_recognition", pixels)
    return render_template('results.html', img=img, result=result, answer=answer)


@main_page_blueprint.route('/car_results', methods=['POST'])
def return_car_results_page():
    files = request.files.getlist('files[]')
    right_files_amount = 8
    images_worker = WorkerWithImages()
    digit_indexes = [1, 2, 3, 6, 7]
    results = []
    answers = []

    if len(files) is not right_files_amount:
            return render_template('index.html', error="Неверное количество файлов!")

    if not InputFilesDAO().is_files_correct(files):
        return render_template('index.html', error="У файлов неправильные расширения!")


    for file, i in zip(files, range(len(files))):
        pixels = images_worker.convert_28_28_image_to_pixels_array(file)
        pixels = images_worker.change_black_to_white(pixels)
        # img = images_worker.convert_image_to_base(file)
        if i in digit_indexes:
            result, answer = recognize_user_input("digit_recognition", pixels)
        else:
            result, answer = recognize_user_input("ru_car_letters_recognition", pixels)
        results.append(result)
        answers.append(str(answer).lower())

    results = zip(results, answers)
    answers = ''.join(answers)
    return render_template('car_results.html', results=results, answers=answers)


if __name__ == '__main__':
    pass
