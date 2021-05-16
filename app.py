import io

from flask import Flask, jsonify, abort, make_response
import requests

import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/nba-api/describe')
def nba_describe():
    nba = pd.read_csv("raw-data/nba_all_elo.csv")
    description = nba.describe()
    return description.to_json()

@app.route('/nba-api/head')
def nba_head():
    nba = pd.read_csv("raw-data/nba_all_elo.csv")
    head = nba.head()
    return head.to_json()\

@app.route('/nba-api/head/<int:num_rows>', methods=['GET'])
def nba_head_rows(num_rows):
    nba = pd.read_csv("raw-data/nba_all_elo.csv")
    head = nba.head(num_rows)
    return head.to_json()

@app.route('/country-api/countries')
def get_countries():
    csv_url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
    try:
        url_content = requests.get(csv_url).content # stream
        # In-memory text streams are also available as StringIO objects
        csv_data = pd.read_csv(io.StringIO(url_content.decode('utf-8')))

        # Option 1
        # raw_json_data = csv_data.to_json(orient='records')
        # return raw_json_data

        # Option 2
        row_count = csv_data.shape[0]
        column_count = csv_data.shape[1]
        column_names = csv_data.columns.tolist()

        final_row_data = []
        for index, rows in csv_data.iterrows():
            final_row_data.append(rows.to_dict())

        json_result = {'rows': row_count, 'cols': column_count, 'colums': column_names, 'rowData': final_row_data}
        return json_result

    except Exception as inst:
        print(type(inst))
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)