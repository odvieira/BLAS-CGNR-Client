import pandas as pd
import numpy as np
import requests
from requests.models import Response
import math
import easygui
import json

class Funcoes(object):
    def __init__(self, user, url):
        super(Funcoes, self).__init__()
        self.user = user
        self.url = url

    def processar_nova_entrada(self):
        # filename = easygui.openfilenamebox()
        filename = "G-1.csv"
        dataFrame = pd.read_csv(filename, header=None)

        sensors = 64
        samples = 794

        aux = input("Número de sensores (64): ")

        if type(aux) is int and aux > 0:
            sensors = aux
        
        aux = input("Número de amostras (794): ")

        if type(aux) is int and aux > 0:
            samples = aux
        
        matrix = dataFrame.values

        k = 0
        for l in range(samples):
            for c in range(sensors):
                gama = 100 + 0.05 * (c+1) * math.sqrt(c+1)
                matrix[k] *= gama
                k += 1

        dataPost = {}
        dataPost['matriz_sinal_g'] = matrix.ravel().tolist()

        response = requests.post(
            self.url + \
                '/cgnr/reconstruir/{0}/{1}'.format(
                    self.user['nome'],
                    str(input("Insira um rótulo para esse arquivo: "))
                ),
            json=dataPost
            )

        return response

    def recuperar_lista_de_imagens(self):
        response = requests.get('{0}/{1}/'.format(
            self.url + '/imagem',
            self.user['nome']
        ))

        result = json.load(response.json())

        # pretty_object = json.dumps(result, indent=4)

        # print(pretty_object)

        print('|| {0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7} ||'.format(
            "Nome"
            "Usuario"
            "Algoritmo"
            "Tempo_Inicio"
            "Tempo_Fim"
            "Pixels"
            "# de Iteracoes"
        ))

        for r in result:
            print(
                '|| {0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7} ||'.format(
                    r['nome'],
                    r['usuario'],
                    r['algoritmo'],
                    r['tempo_inicio'],
                    r['tempo_fim'],
                    r['tamanho_pixels'],
                    r['qntd_iteracoes_executadas']
                )
            )

        print('Digite o nome dos arquivos que deseja salvar,  separado-os por vírgulas: ')

        archive_lst = input('>\t')

        archive_lst = archive_lst.split(',')

        self.baixar_imagens(archive_lst)

        return

    def baixar_imagens(self, list_of_files):
        for f in list_of_files:
            requests.get(
                self.url + '/imagem/' + str(f)
            )

        return

    def consultar_todas_enquete(self):
        pass