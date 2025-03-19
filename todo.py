import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos yet!")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo['task']} (Completed: {todo['completed']})")

def add_todo(task):
    todos = load_todos()
    todos.append({'task': task, 'completed': False})
    save_todos(todos)
    print(f"Added todo: {task}")

def delete_todo(index):
    todos = load_todos()
    try:
        removed_todo = todos.pop(index - 1)
        save_todos(todos)
        print(f"Deleted todo: {removed_todo['task']}")
    except IndexError:
        print("Invalid todo index!")

def mark_completed(index):
    todos = load_todos()
    try:
        todos[index - 1]['completed'] = True
        save_todos(todos)
        print(f"Marked todo as completed: {todos[index - 1]['task']}")
    except IndexError:
        print("Invalid todo index!")
