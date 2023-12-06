import PySimpleGUI as sg
from preces import product as prod
from functions import add

layoutMain = [  [sg.Text("Wabalabadubdub")],
                [sg.Button("Add wares"), sg.Button("Edit stock")],
                [sg.Button("Quit")]]

layoutInput = [ [sg.Text("Preces pievienošana:")],
                [sg.Text("Nosaukums: "), sg.InputText(key="name")],
                [sg.Text("Skaits: "), sg.InputText(key="amountA")],
                [sg.Text("Tips: "), sg.Radio("Detaļa", group_id="add", default=True, key="detala"), sg.Radio("Programmatūra", group_id="add", key="programma")],
                [sg.Button("Add")],
                [sg.Button("Back")] ]

layoutOutput = [[sg.Listbox(values=[], key="output", size=(40,20))],
                [sg.Button("Remove"), sg.InputText(key= "amountR")],
                [sg.Button("Back.")] ]

layout = [[sg.Column(layoutMain, key="Main"), sg.Column(layoutInput, visible=False, key="Input"), sg.Column(layoutOutput, visible=False, key="Output")]]


window = sg.Window('Gain reporter', layout)

Stack = []

while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
                break
        
        if event == "Add wares":
                window[f'Input'].update(visible=True)
                window[f'Main'].update(visible=False)
                
        if event == "Edit stock":
                window[f'Output'].update(visible=True)
                window[f'Main'].update(visible=False)
        
        if event == "Back":
                window[f'Input'].update(visible=False)
                window[f'Main'].update(visible=True)

        if event == "Back.":
                window[f'Output'].update(visible=False)
                window[f'Main'].update(visible=True)

        if event == "Add":
                item = prod(values["name"], values["amountA"], type)
                
                Stack = add(Stack, item)

                list=[]
                for product in Stack:
                        if product.amount != 0:
                                # CHANGE THIS
                                list.append(str(product.amount) + "kg of " + str(product.species) + " which is considered a " + str(product.fruit))
                                # CHANGE THIS

                window["output"].update(values=list)
                

window.close()
