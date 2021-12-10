import requests
from funcoes import Funcoes
from utils import TerminalUtils
import os
import json

url = "http://localhost:8080"

terminal = TerminalUtils()

#Força a criação de um cliente para continuar
print("Escolha um nome de usuario para começar.")
user = input()
print("Bem vindo(a), " + user)

#Gerar chave - desabilitado
#Cadastrar no servidor
user_data = {}
user_data["nome"] = user

response = requests.post(url=url + "/usuario", json=user_data)

if response.status_code == 200:
    print("Logado com sucesso")
else:
    print("Usuario cadastrado com sucesso")

input("\n>> Pressione Enter para prosseguir <<")

# if response.status_code >= 200 and response.status_code <= 299:
#     #Sucesso
#     print("Usuario criado com sucesso!")
#     print("Status Code", response.status_code)
#     print("Texto", response.text)
#     print("JSON", response.json())

#Inicializa menu
while True:
    escolha = terminal.menu()

    if escolha == 1:  
        Funcoes.processar_nova_entrada(user)
    elif escolha == 2:
        Funcoes.recuperar_lista_de_imagens(user)
    elif escolha == 3:
        Funcoes.baixar_imagens()
    elif escolha == 4:
        Funcoes.consultar_todas_enquete(user)
    elif escolha == 9:
        os._exit(0)
    else:
        print("Opção inválida.")
