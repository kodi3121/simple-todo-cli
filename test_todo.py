import os
import pytest
from todo import load_todos, save_todos, add_todo, delete_todo

TEST_FILE = 'test_todos.json'

def test_add_todo():
    save_todos([])  # Reset todos
    add_todo('Test Task')
    todos = load_todos()
    assert len(todos) == 1
    assert todos[0]['task'] == 'Test Task'

def test_delete_todo():
    save_todos([{'task': 'Test Task', 'completed': False}])  # Add a test task
    delete_todo(1)  # Delete the task
    todos = load_todos()
    assert len(todos) == 0

@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
