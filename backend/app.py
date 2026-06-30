from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json

    task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": False
    }

    tasks.append(task)

    return jsonify(task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    for task in tasks:

        if task['id'] == id:

            task['completed'] = not task['completed']

            return jsonify(task)

    return jsonify({"message":"Task not found"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    global tasks

    tasks = [task for task in tasks if task['id'] != id]

    return jsonify({"message":"Deleted"})


if __name__ == '__main__':
    app.run(debug=True)