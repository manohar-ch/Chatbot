from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

@APP.get("/")
def index():
    """ Rendering to template for home page """
    return render_template('base.html')

@APP.post("/predict")
def predict():
    """ Chat home page """
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    APP.run()
