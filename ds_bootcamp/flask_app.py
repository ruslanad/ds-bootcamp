from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_ruslana():
        return "Hi Ruslana!", 200

    @app.route("/bye")
    def props():
        return "You are great!", 200

    return app
# FLASK_APP=bootcamp_ds/flask_app.py flask run
