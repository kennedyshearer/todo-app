import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightBrown10")

layout = [  [sg.Text('', key='clock')],
            [sg.Text("Type in a to-do:")],
            [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")],
            [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True,
                        size=[45, 10]), sg.Button("Edit"), sg.Button("Remove")],
            [sg.Button("Exit")]  ]

window = sg.Window('To-Do App', layout, font=('Helvetica', 18))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo.capitalize())
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todos_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todos_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 18))
        case "Remove":
            try:
                todos_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 18))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()