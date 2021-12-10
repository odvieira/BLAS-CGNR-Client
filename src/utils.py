import os, platform

class TerminalUtils(object):
	def __init__(self, *args):
			super(TerminalUtils, self).__init__(*args)

			self.term_size = os.get_terminal_size()

			pass
				
	def clear(self):
		if platform.system() == 'Windows':
				os.system('cls')
		else:
				os.system('clear')

	def menu(self):
		self.clear()

		print("||              MENU                  ||")
		print('||====================================||')
		print("||    [1] Processar nova entrada      ||")
		print("||    [2] Recuperar lista de imagens  ||")
		print("||    [0] Encerrar aplicação          ||")
		print('||====================================||')
		op = int(\
		input("Digite o número da ação para selecioná-la: ")
		)

		self.clear()

		return op
