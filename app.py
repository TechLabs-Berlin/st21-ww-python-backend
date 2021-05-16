from flask import Flask, jsonify, abort, make_response
import flask.scaffold
import pandas as pd
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, fields
app = Flask(__name__)

api = Api(app)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, cheese, bananas',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to learn python to finish the project',
        'done': False
    }
]

class TaskListAPI(Resource):
    def get(self):
        return {'tasks': tasks}
    def put(self):
        pass

class TaskAPI(Resource):
    def get(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        return {'task': task[0]}
    def put(self, id):
        pass
    def delete(self, id):
        pass

api.add_resource(TaskListAPI, '/todo/api/v2/tasks')
api.add_resource(TaskAPI, '/todo/api/v2/tasks/<int:id>')

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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)