from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tasks = ["Goto the mall to pick up books", "Task 2"]


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    if task_id >= 0 and task_id < len(tasks):
        tasks[task_id] = "[X] " + tasks[task_id]
        return jsonify({'message': 'Task marked as completed!'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id >= 0 and task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully!'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
