import functions
import FreeSimpleGUI as sg

layout = [  [sg.Text("Type in a to-do:")],
            [sg.InputText(tooltip="Enter todo"), sg.Button("Add")]    ]

window = sg.Window('To-Do App', layout)
window.read()
window.close()