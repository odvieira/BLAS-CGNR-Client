import os
import requests
from utils import TerminalUtils
from funcoes import Funcoes

url = "http://localhost:8080"

terminal = TerminalUtils()

login = False

while not login:
    terminal.clear()
    
    #Força a criação de um cliente para continuar
    print("Escolha um nome de usuario para começar.")
    user = input()

    terminal.clear()
    print("\n\tBem vindo(a), " + user)

    #Gerar chave - desabilitado
    #Cadastrar no servidor
    user_data = {}
    user_data["nome"] = user

    try:
        response = requests.post(url=url + "/usuario", json=user_data)

        terminal.clear()

        login = True

        if response.status_code == 200:
            print("Logado com sucesso!")
        elif response.status_code == 201:
            print("Usuario cadastrado com sucesso!")
        elif response.status_code >= 400:
            print("Houve um erro na autenticação.")
            login = False
    except:
        login = True

terminal.prompt_continuar()

terminal.clear()

f = Funcoes(user_data, url)

#Inicializa menu
while True:
        escolha = terminal.menu()
        
        if escolha not in range(9):
                escolha = -1

        if escolha == 1:
                f.processar_nova_entrada()
        elif escolha == 2:
                f.recuperar_lista_de_imagens()
        elif escolha == 0:
                os._exit(0)
        else:
                terminal.err_msg("Opção inválida.")