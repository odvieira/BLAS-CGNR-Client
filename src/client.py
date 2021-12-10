import requests
from funcoes import Funcoes
from utils import TerminalUtils
import os
import json

url = "http://localhost:8080"

terminal = TerminalUtils()

login = False

while not login:
    #Força a criação de um cliente para continuar
    print("Escolha um nome de usuario para começar.")
    user = input()
    print("Bem vindo(a), " + user)

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

input("\n>> Pressione Enter para prosseguir <<")

terminal.clear()

f = Funcoes(user, url)

#Inicializa menu
while True:
    escolha = terminal.menu()

    if escolha == 1:
        f.processar_nova_entrada()
    elif escolha == 2:
        f.recuperar_lista_de_imagens()
    elif escolha == 3:
        f.baixar_imagens()
    elif escolha == 4:
        f.consultar_todas_enquete()
    elif escolha == 9:
        os._exit(0)
    else:
        print("Opção inválida.")
