import os
import pandas as pd
import numpy as np
import requests
import math
import base64
from cv2 import cv2
from utils import TerminalUtils

class Funcoes(object):
    def __init__(self, user, url):
        super(Funcoes, self).__init__()
        self.user = user
        self.url = url
        self.terminal = TerminalUtils()

    def processar_nova_entrada(self):
        # filename = easygui.openfilenamebox()
        filename = input('Insira o caminho relativo do arquivo de entrada: ')
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

        rot = False

        while not rot:
            try:
                rotulo = str(input("Insira um rótulo para esse arquivo: ")).strip(
                ',').strip('/').strip('\\').strip('.')

                assert rotulo.isalnum

                rot = True
            except print(0):
                rot = False


        response = requests.post(
            self.url +
            '/cgnr/reconstruir/{0}/{1}'.format(
                self.user['nome'],
                rotulo
            ),
            json=dataPost
        )

        return response

    def recuperar_lista_de_imagens(self):
        response = requests.get('{0}/{1}/'.format(
            self.url + '/imagem',
            self.user['nome']
        ))

        result = response.json()

        print('| {0}\t\t\t{1}\t\t\t{2}\t\t\t{3}\t\t\t{4}\t\t\t{5}\t\t\t{6} |'.format(
            "Nome",
            "Usuario",
            "Algoritmo",
            "Tempo_Inicio",
            "Tempo_Fim",
            "Pixels",
            "# de Iteracoes"
        ))

        print('=' * self.terminal.term_size.columns)

        for r in result:
            print(
                '| {0}\t|\t{1}\t\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\t|\t{6} |'.format(
                    r['nome'],
                    r['usuario'],
                    r['algoritmo'],
                    r['tempo_inicio'],
                    r['tempo_fim'],
                    r['tamanho_pixels'],
                    r['qntd_iteracoes_executadas']
                )
            )
        
        print('=' * self.terminal.term_size.columns)

        print('Digite o nome dos arquivos que deseja salvar, separado-os por vírgulas: ')

        archive_lst = input('>\t')

        archive_lst = archive_lst.split(',')

        df = pd.DataFrame(result)

        if not os.path.exists('./out/' + df['usuario'].values[0]):
            os.mkdir('./out/{0}'.format(df['usuario'].values[0]))

        for f in archive_lst:
            aux = df[df['nome'] == f]
            aux['img']

            string = aux['img'].values[0]
            # string = data_data
            
            jpg_original = base64.b64decode(string.encode('ascii'))
            jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
            img = cv2.imdecode(jpg_as_np, flags=1)
            
            print('Salvando ' + aux['nome'] + '...')

            cv2.imwrite('{1}/{0}.jpg'.format(
                aux['nome'].to_string(),
                './out/{0}'.format(df['usuario'].values[0])
                ),
            img)

        return