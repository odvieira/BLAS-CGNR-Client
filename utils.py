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

	def print_table(self, df):
		print('=' * self.term_size.columns)
		print('')

		print(df)
		
		print('')
		print('=' * self.term_size.columns)

	def prompt_continuar(self):
		input("\n>> Pressione Enter para prosseguir <<")

	def err_msg(self, msg):
		self.clear()
		print("\n\t{0}".format(msg))
		self.prompt_continuar()

	def menu(self):
		self.clear()

		print('\n\n')
		print('\t\t ======================================')
		print("\t\t||              MENU                  ||")
		print('\t\t||====================================||')
		print("\t\t||    [1] Processar nova entrada      ||")
		print("\t\t||    [2] Recuperar lista de imagens  ||")
		print("\t\t||    [0] Encerrar aplicação          ||")
		print('\t\t ======================================')
		op = int(\
		input("\t\tDigite o número da ação para selecioná-la: ")
		)

		self.clear()

		return op
