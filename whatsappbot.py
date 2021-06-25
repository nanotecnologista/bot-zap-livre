# importar as bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep  # lib tempo
from datetime import datetime  # lib do calendario
from PySimpleGUI import PySimpleGUI as sg #interface
import pandas as pd  # lib pandas com o apelido carinhoso de pd, haha já sou intima
import mensagemParabens as msgP  # meu script
import mensagemAulasExperimentais as msgA
import mensagemPersonalizada as msgPerson
import clipboard
import os

def buscar_contato(contato):
    driver = chamandoDriver()
    try:
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        sleep(1)
        campo_pesquisa.click()
        sleep(1)
        campo_pesquisa.send_keys(contato)
        sleep(1)
        campo_pesquisa.send_keys(Keys.ENTER)

    except Exception as Erro:
        print('404 error: ', Erro)

def enviar_mensagem(mensagem):

    clipboard.copy(mensagem)
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    sleep(1)
    campo_mensagem[1].send_keys(Keys.CONTROL + 'v')
    sleep(1)
    campo_mensagem[1].send_keys(Keys.ENTER)

def lendoAniversariantes(plan, quantidade, data_hoje):

    linhas = 0  # contadora

    while (linhas <= quantidade):
        data_aniversario = plan["Data"][linhas]
        if data_aniversario == data_hoje:
            numero_aniversariante = plan["Numero"][linhas]
            nome_aniversariante = plan["Nome"][linhas]
            adulto_ou_crianca = plan["Adulto"][linhas]
            if adulto_ou_crianca == 0:
                texto_niver = False
            else:
                texto_niver = True
            mensagem = msgP.InserindoNome(texto_niver, nome_aniversariante)
            contato = int(numero_aniversariante)
            buscar_contato(contato)
            enviar_mensagem(mensagem)

        linhas = linhas+1
    deNovo()

def lendoAulasExperimentais(plan, quantidade, data_hoje):

    linhas = 0  # contadora

    while (linhas <= quantidade):
        data_aula = plan["Data"][linhas].date()
        diferenca = ((data_hoje - data_aula).days)
        if diferenca == 1:    
            numero = plan["Numero"][linhas]
            nomeAdulto = plan["NomeAdulto"][linhas]
            servico = plan["Servico"][linhas]
            if servico == 'Natação':
                nomeCrianca = plan["NomeCrianca"][linhas]
            else:
                nomeCrianca = False
            mensagem = msgA.InserindoNome( nomeAdulto, nomeCrianca, servico)
            contato = (int(numero))
            buscar_contato(contato)
            enviar_mensagem(mensagem)

        linhas = linhas+1
    deNovo()

def mensagemPersonalizada(plan, quantidade):

    linhas = 0  # contadora
    caminho= (r'.\planilha\mensagem.txt') 
    texto = open(caminho,'r')

    while (linhas <= quantidade):
        numero = plan["Numero"][linhas]
        nome = plan["Nome"][linhas]
        mensagem = msgPerson.InserindoNome(texto, nome)
        contato = (int(numero))
        buscar_contato(contato)
        enviar_mensagem(mensagem)

        linhas = linhas+1
    deNovo()

def oQueFazer(o_que_fazer): 
    if (o_que_fazer == 1):
        plan = pd.read_excel(r".\planilha\aniversariantes.xlsx")
        quantidade = len(plan)-1
        lendoAniversariantes(plan, quantidade, data_hoje)

    elif (o_que_fazer == 2):
        plan = pd.read_excel(r".\planilha\aulasExperimentais.xlsx")
        quantidade = len(plan)-1
        lendoAulasExperimentais(plan, quantidade, data_hoje)

    elif (o_que_fazer == 3):
        plan = pd.read_excel(r".\planilha\mensagemPersonalizada.xlsx")
        quantidade = len(plan)-1
        mensagemPersonalizada(plan, quantidade)

    else:
        print('nenhum valor válido foi inserido')

def start():
    try:
        #Layout
        sg.theme('Reddit')
        layout =[
            [sg.Text(' Enviar mensagem para:\n [1]Aniversariantes \n [2]Aulas Experimentais\n [3]Mensagem Personalizada\n')],
            [sg.Input()],
            [sg.Button('Iniciar')]
        ]

        #Janela
        janela = sg.Window('Disparo Mensagens', layout)

        #ler eventos
        eventos, valor = janela.read()
        if eventos == sg.WIN_CLOSED:
            janela.close()
        if eventos == 'Iniciar':
            o_que_fazer = int(valor[0])
            janela.close()

    except Exception as erro:
        print("\nFavor, digitar o número correspondente a uma das opções\n")
        o_que_fazer = int(input('Enviar mensagem para:\n [1]Aniversariantes \n [2]Aulas Experimentais\n [3]Mensagem Personalizada\n'))
    
    oQueFazer(o_que_fazer)

def deNovo():
    deNovo = sg.popup_yes_no ('Fazer outra operação?')
    if (deNovo == 'Yes'):
        start()
    else:
        os.system('pause')
        driver.close()

def chamandoDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "usuario")
    options.add_argument(r"user-data-dir={}".format(profile))

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://web.whatsapp.com/')
    os.system('pause')

    return driver


## Começa Aqui
data_hoje = datetime.today().date()
start()
dasjkfjsakfjdfdsg
