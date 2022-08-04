import PySimpleGUI as sg

def calcular_equacao(equacao):

  resultado = eval(input())
  print(equacao + f"\n tipo equacao: {type(equacao)}")
  
  return resultado
 


sg.theme('DarkAmber')   
layout = [  [sg.Text("Calculadora", justification= "center", size=(400,1))],
            [sg.InputText(size=(10,1)), sg.Button("="), sg.Text("         ", size=(0,1), key="print", background_color="green")],
         ]

window = sg.Window('CalcLab', layout, size= (400,100))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    window['print'].update(str(calcular_equacao(values[0])))