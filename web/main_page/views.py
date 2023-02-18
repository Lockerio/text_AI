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

    output = recognize_user_input("digit_recognition", pixels)
    result = output[0]
    answer = output[1]

    return render_template('results.html', result=result, answer=answer)


if __name__ == '__main__':
    pass
