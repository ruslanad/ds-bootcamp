from flask import Flask, jsonify
import os
import yaml


dir_path = os.path.dirname(os.path.realpath(__file__))
MAX_VALUE = 10000
MIN_VALUE = 0


def create_app():
    app = Flask(__name__)
    with open(os.path.join(dir_path, 'yamls', 'ruslana_model.yaml'), 'r') as f:
        model_config = yaml.load(f, Loader=yaml.SafeLoader)

    @app.route("/ruslana")
    def hello_ruslana():
        return "Hi Ruslana!", 200

    @app.route("/props")
    def props():
        return "You are great!", 200

    @app.route("/ruslana_model/<submodel>/<x_1>")
    def ruslana_yaml_model(submodel, x_1):
        x_1 = int(x_1)

        if x_1 > MAX_VALUE:
            return f"Value {x_1} > {MAX_VALUE}", 400
        elif x_1 < MIN_VALUE:
            return f"Value {x_1} < {MIN_VALUE}", 400
        try:
            submodel = model_config[submodel]
        except(KeyError):
            return 'Model not found', 404
        dict_ = {'score': submodel['a_1']+submodel['b_1'] * x_1}
        return jsonify(dict_)

    return app
# FLASK_APP=bootcamp_ds/flask_app.py flask run
