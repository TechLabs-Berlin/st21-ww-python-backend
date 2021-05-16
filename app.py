from flask import Flask, jsonify, abort, make_response
import flask.scaffold
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

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)