# from PySimpleGUI import PySimpleGUI as sg

# #Layout
# sg.theme('Reddit')
# layout =[
#     [sg.Text('teste')],
#     [sg.Input(key= 'oQueFazer')]
#     [sg.Button('Iniciar')]
# ]

# #Janela
# janela = sg.Window('Tela de login', layout)

# #ler eventos
# while True:
#     eventos, valor = janela.read()
#     if eventos == sg.WIN_CLOSED:
#         break
#     if eventos == 'Iniciar':
#         print ("Parou aqui")

# def InserindoNome (texto, nome):
#     try:
#         texto = texto.replace('[nome]', nome)
#         return str(texto)
#     except Exception as erro:
#         return str(texto)

# texto = """ Olá, [nome]!
# Eu sou a Jujuba Nanotech mais gata do mundo"""

# nome= 'Julia'

# mensagem = InserindoNome(texto, nome)
# print (mensagem)


# data_hoje = date.today()
# data_teste = date.today()
# print (data_teste)
# diferenca = abs((data_hoje - data_teste).days)
# print (diferenca)

# from datetime import date, datetime
# import pandas as pd

# plan = pd.read_excel(r".\planilha\aulasExperimentais.xlsx")
# data1 = plan['Data'][0].date()
# data2 = datetime.today().date()

# print(data1)
# print(data2)
# diferenca = ((data2 - data1).days)
# print (diferenca)
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup_yes_no      

# layout = [[sg.Text('My one-shot window.')],      
#                  [sg.InputText()],
#                  [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],    
#                  [sg.Submit(), sg.Cancel()]]      

# window = sg.Window('Window Title', layout)    

# event, values = window.read()    
# window.close()

# text_input = values[0]    
# sg.popup('You entered', text_input)

#event, values = sg.Window('Get filename example', [sg.popup_yes_no]).read(close=True)
#sg.Window([sg.popup_yes_no (bu)] ).read
# sg.popup('popup')  # Shows OK button
# sg.popup_ok('popup_ok')  # Shows OK button
# sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
# sg.popup_cancel('popup_cancel')  # Shows Cancelled button
# sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
# sg.popup_error('popup_error')  # Shows red error button
# sg.popup_timed('popup_timed')  # Automatically closes
# sg.popup_auto_close('popup_auto_close')  #

values = sg.popup_yes_no('Fazer outra operação?')  # Shows Yes and No buttons
print (values)
if values == 'Yes':
    print ("foi")
elif values == True:
    print ("...")
else:
    print ('tenta outra')