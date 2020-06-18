import json
from flask import Flask, request, Response, flash, jsonify
from waitress import serve


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'The app is running...\n'

if __name__ == "__main__":

    serve(app, host='0.0.0.0', port=8080)