# importar as bibliotecas
from logging import exception
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep  # lib tempo
from datetime import date  # lib do calendario
import pandas as pd  # lib pandas com o apelido carinhoso de pd, haha já sou intima
import mensagemParabens as msgP  # meu script
import mensagemVencidos as msgV  # meu outro script
import mensagemAulasExperimentais as msgA
import mensagemPersonalizada as msgPerson
import clipboard
import os

def buscar_contato(contato):
    try:
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        sleep(1)
        campo_pesquisa.click()
        sleep(1)
        campo_pesquisa.send_keys(contato)
        sleep(1)
        campo_pesquisa.send_keys(Keys.ENTER)
    except Exception as Erro:
        print(f'404 error: ', Erro)

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
            #print (mensagem)
            contato = (int(numero_aniversariante))
            buscar_contato(contato)
            enviar_mensagem(mensagem)

        linhas = linhas+1

def lendoVencidos(plan, quantidade, data_hoje):

    linhas = 0  # contadora

    while (linhas <= quantidade):

        data_vencimento = plan["Vencimento"][linhas]
        dia_vencimento = data_vencimento.strftime('%d')
        dia_hoje = data_hoje.strftime('%d')

        if dia_vencimento == dia_hoje:
            data_vencimento = data_hoje.strftime('%d/%m') 
            numero = plan["Numero"][linhas]
            nomeAdulto = plan["NomeAdulto"][linhas]
            servico = plan["Servico"][linhas]
            if servico == 'Natação':
                nomeCrianca = plan["NomeCrianca"][linhas]
            else: 
                nomeCrianca = None
            mensagem = msgV.InserindoNome(nomeAdulto, nomeCrianca, data_vencimento, servico)
            contato = (int(numero))
            buscar_contato(contato)
            enviar_mensagem(mensagem)

        linhas = linhas+1

def lendoAulasExperimentais(plan, quantidade, data_hoje):

    linhas = 0  # contadora

    while (linhas <= quantidade):
        data_aula = plan["Data"][linhas]
        if data_aula == data_hoje:    
            numero = plan["Numero"][linhas]
            nomeAdulto = plan["NomeAdulto"][linhas]
            servico = plan["Servico"][linhas]
            if servico == 'Natação':
                nomeCrianca = plan["NomeCrianca"][linhas]
            else:
                nomeCrianca = False
            mensagem = msgA.InserindoNome(
                nomeAdulto, nomeCrianca, servico)
            #print (mensagem)
            contato = (int(numero))
            buscar_contato(contato)
            enviar_mensagem(mensagem)

        linhas = linhas+1

def mensagemPersonalizada(plan, quantidade):

    linhas = 0  # contadora
    caminho= (r'.\planilha\mensagem.txt') 
    texto = open(caminho,'r')

    while (linhas <= quantidade):
        numero = plan["Numero"][linhas]
        nome = plan["Nome"][linhas]
        mensagem = msgPerson.InserindoNome(texto, nome)
        #print (mensagem)
        contato = (int(numero))
        buscar_contato(contato)
        enviar_mensagem(mensagem)

        linhas = linhas+1


## Começa Aqui
data_hoje = date.today()

def interface(iniciando=True):
    os.system('cls' if os.name == 'nt' else 'clear')
    if (iniciando == True):
        print('Enviar mensagem para:\n [1]Aniversariantes \n [2]Vencidos\n [3]Aulas Experimentais\n [4]Mensagem Personalizada\n')
        o_que_fazer = int(input("Escolha uma opção: "))
        if (o_que_fazer in [1,2,3,4]):
            if (o_que_fazer == 1):
                plan = pd.read_excel(r".\planilha\aniversariantes.xlsx")
                quantidade = len(plan)-1
                lendoAniversariantes(plan, quantidade, data_hoje)
                sleep(1)
                interface(iniciando=False)
            elif (o_que_fazer == 2):
                plan = pd.read_excel(r".\planilha\vencidos.xlsx")
                quantidade = len(plan)-1
                lendoVencidos(plan, quantidade, data_hoje)
                sleep(1)
                interface(iniciando=False)
            elif (o_que_fazer == 3):
                plan = pd.read_excel(r".\planilha\aulasExperimentais.xlsx")
                quantidade = len(plan)-1
                lendoAulasExperimentais(plan, quantidade, data_hoje)
                sleep(1)
                interface(iniciando=False)

            elif (o_que_fazer == 4):
                plan = pd.read_excel(r".\planilha\mensagemPersonalizada.xlsx")
                quantidade = len(plan)-1
                mensagemPersonalizada(plan, quantidade)
                sleep(1)
                interface(iniciando=False)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Comando Invalido.')
            sleep(1.3)
            interface(iniciando=True)
    elif (iniciando == False):
        print("Deseja voltar o menu principal:\nSim ou Não")
        o_que_fazer = str(input("Escolha uma opção: "))
        if (o_que_fazer.lower() in ["sim", "s"]):
            interface(iniciando=True)
        else:
            print("Encerrando Projeto")
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"user-data-dir={os.path.join(os.getcwd(), 'profile', 'usuario')}")
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    driver.get("https://web.whatsapp.com/")
    try:
        interface(iniciando=True)
    except KeyboardInterrupt:
            driver.close()
            print("\nEncerrando Sistema ...")
#teste
#testedoteste