from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/raw-data/describe')
def raw_data():
    nba = pd.read_csv("data/nba_all_elo.csv")
    info = nba.describe()
    return info.to_json()

if __name__ == '__main__':
    app.run(debug=True)