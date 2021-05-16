from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, cheese, bananas',
        'done': False
    },{
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to learn python to finish the project',
        'done': False
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)