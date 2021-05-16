from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)