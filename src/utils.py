import os, platform


class TerminalUtils(object):
	def __init__(self, *args):
			super(TerminalUtils, self).__init__(*args)

			pass
				
	def clear(self):
		if platform.system() == 'Windows':
				os.system('cls')
		else:
				os.system('clear')

	def menu(self):
		print("====================================================")
		print("||                      MENU                      ||")
		print("====================================================")
		print("|| [1] Processar nova entrada                     ||")
		print("|| [2] Recuperar lista de imagens                 ||")
		print("|| [3] Baixar imagens                             ||")
		print("|| [0] Encerrar apliciação                        ||")
		print("====================================================")
		op = int(\
		input("Digite o número para selecionar a ação:             ")
		)

		self.clear()

		return op
