from functions import get_todos, write_todos
import time

date_time = time.strftime("%b %d, %Y %H:%M:%S")
print("Today is: " + date_time)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.capitalize() + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.capitalize() + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. The selection should be the NUMBER of that item.")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[6:])

            todos = get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo: {todo_to_remove} - was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("See ya later!")