import sys
from todo import add_todo, list_todos, delete_todo, mark_completed

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py [add|list|delete|complete]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "list":
        list_todos()
    elif command == "add" and len(sys.argv) > 2:
        task = ' '.join(sys.argv[2:])
        add_todo(task)
    elif command == "delete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2])
            delete_todo(index)
        except ValueError:
            print("Please provide a valid index.")
    elif command == "complete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2])
            mark_completed(index)
        except ValueError:
            print("Please provide a valid index.")
    else:
        print("Invalid command or missing arguments.")

if __name__ == '__main__':
    main()
