
import os

filepath = os.path.join(os.path.dirname(__file__), 'todos.txt')

def get_todos():
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg):
    """ Write the to-do items list in t3.13he text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
