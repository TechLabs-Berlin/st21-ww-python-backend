from flask import Flask, jsonify
import pandas as pd

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



if __name__ == '__main__':
    app.run(debug=True)