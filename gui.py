
import PySimpleGUI as sg

event, values = sg.Window('CACS Reporting Tool').Layout([[sg.Text('Select the file you wish to load')],
                                                   [sg.Button('YES'),sg.CloseButton('NO')]]).Read()



def menu_scratch():
    layout = [[sg.Text('My one-shot window.')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    window.close()
    key2 = values[0].capitalize()
    print(key2)
    window.close()
    values2 = []
    recipe = {key2: values2}

    layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout)

    while True:
        event, values1 = window.read()
        if event == 'Show':
            recipe.setdefault(key2,[]).append(values1)
            window.close()

        if event == sg.WIN_CLOSED or event == 'Exit':
            print(recipe)
            break


    while True:
        ans2 = input("Add recipe? Y/N ").capitalize()
        if ans2 == 'Y':
            key2 = input("What is it? ").capitalize()
            values2 = []
            recipe[key2] = values2

            while True:
                values2 = input("Add ingredient. Type Done to save: ").capitalize()
                if values2 != "Done":
                    recipe.setdefault(key2,[]).append(values2)
                    continue
                else:
                    break
            continue
        elif ans2 == 'N':
            break
        else:
            print('Error, try again')
            continue


    with open("menu.json", "a+") as file:
        json.dump(recipe, file)


if event == 'YES':
    menu_scratch()


