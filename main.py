from flask import Flask
from web.main_page.views import main_page_blueprint


app = Flask(__name__)
app.register_blueprint(main_page_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
