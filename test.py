# %%
import os
import pandas as pd
import numpy as np
import requests
import math
import base64
from cv2 import cv2
from utils import TerminalUtils
# %%
lst = []

for i in range(7):
		ab = {}
		ab["Nome"]='info ' + str(i)
		ab["Usuario"]='infasdaso ' + str(i)
		ab["Algoritmo"]='info ' + str(i)
		ab["Tempo_Inicio"]='infdasdasdaso ' + str(i)
		ab["Tempo_Fim"]='info asdasdasdsadas ' + str(i)
		ab["Pixels"]='info ' + str(i)
		ab["# de Iteracoes"]='info ' + str(i)

		lst.append(ab)

dat = pd.DataFrame(lst)

print(dat)


        # print('| {0}\t\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6} |'.format(
        #     "Nome",
        #     "Usuario",
        #     "Algoritmo",
        #     "Tempo_Inicio",
        #     "Tempo_Fim",
        #     "Pixels",
        #     "# de Iteracoes"
        # ))

        # print('=' * self.terminal.term_size.columns)

        # for r in result:
        #     print(
        #         '| {0}\t|\t{1}\t\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\t|\t{6} |'.format(
        #             r['nome'],
        #             r['usuario'],
        #             r['algoritmo'],
        #             r['tempo_inicio'],
        #             r['tempo_fim'],
        #             r['tamanho_pixels'],
        #             r['qntd_iteracoes_executadas']
        #         )
        #     )