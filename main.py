import PySimpleGUI as sg
from preces import product as prod
from functions import add

layoutMain = [  [sg.Text("Wabalabadubdub")],
                [sg.Button("Add wares"), sg.Button("Edit stock")],
                [sg.Button("Quit")]]

layoutInput = [ [sg.Text("Preces pievienošana:")],
                [sg.Text("Nosaukums: "), sg.Push(), sg.InputText(key="name")],
                [sg.Text("Skaits: "), sg.Push(), sg.InputText(key="amountA")],
                [sg.Text("Tips: "), sg.Radio("Detaļa", group_id="add", default=True, key="detala"), sg.Radio("Programmatūra", group_id="add", key="programma")],
                [sg.Button("Add"), sg.Push(), sg.Button("Back")] ]

layoutOutput = [[sg.Listbox(values=[], key="output", size=(60,20))],
                [sg.Button("Remove"), sg.InputText(key= "amountR"), sg.Push(), sg.Button("Back.")] ]

layout = [[sg.Column(layoutMain, key="Main"), sg.Column(layoutInput, visible=False, key="Input"), sg.Column(layoutOutput, visible=False, key="Output")]]


window = sg.Window('Stock reporter', layout)

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
                tip = "none"

                for thing in values:
                        if values[thing] == True:
                                tip = thing
                                break

                item = prod(values["name"], values["amountA"], tip)
                
                Stack = add(Stack, item)

                list=[]
                for product in Stack:
                        if product.amount != 0:
                                list.append(str(product.amount) + " of " + str(product.name) + " which is considered a " + str(product.type))

                window["output"].update(values=list)
                
        if event == "Remove":
                for item in Stack:
                        if item.compare() == values["output"][0]:
                                if item.take(values["amountR"]):
                                        if item.amount == 0:
                                                Stack.remove(item)
                                break
                                     
                list=[]
                for product in Stack:
                        if product.amount != 0:
                                list.append(str(product.amount) + " of " + str(product.name) + " which is considered a " + str(product.type))

                window["output"].update(values=list)   
                

window.close()
