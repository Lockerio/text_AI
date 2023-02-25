from flask import render_template, Blueprint, request
from utils.work_with_images import WorkerWithImages
from AI.main import recognize_user_input


main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates', static_folder='../static')


@main_page_blueprint.route('/')
def return_main_page():
    return render_template('index.html')


@main_page_blueprint.route('/results', methods=['POST'])
def return_results_page():
    raw_img = request.files.get("picture")
    images_worker = WorkerWithImages()

    # file
    if raw_img:
        pixels = images_worker.convert_28_28_image_to_pixels_array(raw_img)

    # base
    else:
        raw_img = request.form["picture"]
        raw_pixels = images_worker.convert_28_28_image_to_pixels_array(raw_img)
        pixels = images_worker.change_black_to_white(raw_pixels)

    img = images_worker.convert_image_to_base(raw_img)
    result, answer = recognize_user_input("digit_recognition", pixels)
    return render_template('results.html', img=img, result=result, answer=answer)


@main_page_blueprint.route('/car_results', methods=['POST'])
def return_car_results_page():
    files = request.files.getlist('files[]')
    images_worker = WorkerWithImages()
    digit_indexes = [1, 2, 3, 6, 7]
    results = []
    answers = []

    for file, i in zip(files, range(len(files))):
        pixels = images_worker.convert_28_28_image_to_pixels_array(file)
        pixels = images_worker.change_black_to_white(pixels)
        # img = images_worker.convert_image_to_base(file)
        if i in digit_indexes:
            result, answer = recognize_user_input("digit_recognition", pixels)
        else:
            result, answer = recognize_user_input("ru_car_letters_recognition", pixels)
        print(i)
        results.append(result)
        answers.append(str(answer).lower())

    answers = ''.join(answers)
    return render_template('car_results.html', results=results, answers=answers)


if __name__ == '__main__':
    pass
