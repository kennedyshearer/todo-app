import functions
import FreeSimpleGUI as sg

layout = [  [sg.Text("Type in a to-do:")],
            [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")]    ]

window = sg.Window('To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo.capitalize())
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()