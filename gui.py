import PySimpleGUI as sg
import json

window = sg.Window('CACS Reporting Tool').Layout([[sg.Text('Add recipe?')],
                                                   [sg.Button('YES'),sg.CloseButton('NO')]])
event, values = window.read()
window.close()


def menu_scratch():
    layout = [[sg.Text('What is it?')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Recipe Creator', layout)

    event, values = window.read()
    window.close()
    key2 = values[0].capitalize()
    window.close()
    values2 = []
    recipe = {key2: values2}

    layout = [[sg.Text('Type in ingredient here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-', do_not_clear=False)],
              [sg.Button('Add'), sg.Button('Exit')]]

    window = sg.Window('Recipe Creator', layout)

    while True:
        event, ing_values = window.read()
        if event == 'Add':
            ing_vals = list(ing_values.values())
            ingredient = ing_vals[0].capitalize()
            recipe.setdefault(key2,[]).append(ingredient)
            continue

        if event == sg.WIN_CLOSED or event == 'Exit':
            print(recipe)
            window.close()
            break
    window.close()


    with open("menu.json", "a+") as file:
        json.dump(recipe, file)


if event == 'YES':
    menu_scratch()

window.close()





