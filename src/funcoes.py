import pandas as pd
import numpy as np
import requests
from requests.models import Response
from tkinter import Tk    # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import math
import easygui

class Funcoes(object):
    def __init__(self, user, url):
        super(Funcoes, self).__init__()
        self.user = user
        self.url = url

    def processar_nova_entrada(self):
        # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        # filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        # print(filename)        

        filename = easygui.fileopenbox()
        dataFrame = pd.read_csv(filename)

        sensors = 64
        samples = 794

        aux = input("Número de sensores (64): ")

        if type(aux) is int and aux > 0:
            sensors = aux
        
        aux = input("Número de amostras (794): ")

        if type(aux) is int and aux > 0:
            samples = aux
        
        matrix = dataFrame.values

        for c in range(sensors):
            for l in range(samples):
                gama = 100 + 0.05 * l * math.sqrt(l)

                matrix[l * sensors + c] *= gama

        dataPost = {}
        dataPost['matriz_sinal_g'] = matrix.dumps()

        response = requests.post(
            self.url + \
                '/cgnr/reconstruir/{0}/{1}'.format(
                    self.user['name'],
                    str(input("Insira um rótulo para esse arquivo: "))
                ),
            data=dataPost
            )

        return response

    def recuperar_lista_de_imagens(self):
        pass

    def baixar_imagens(self):
        pass

    def consultar_todas_enquete(self):
        pass
