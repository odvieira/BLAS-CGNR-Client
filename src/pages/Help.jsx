import React from 'react'
import '../scss/Help.scss'

function Help() {
	return (
		<div className="Help">
			<div className="InfoBox">
				<h1>Cliente</h1>
				<p>
					Implementar uma aplicação cliente com as seguintes características:
				</p>
				<ul>
					<li>Carregar a partir de um arquivo local um sinal de ultrassom;</li>
					<li>Realizar o controle de ganho de sinal;</li>
					<li>Enviar o sinal tratado para um servidor de reconstrução de imagens;</li>
					<li>Carregar a partir do servidor todas as imagens reconstruídas por um usuário.</li>
					<li>Selecionar uma ou mais imagens e salvar localmente.</li>
				</ul>
			</div>
			<div className="InfoBox">
				<h1>Servidor</h1>
				<p>
					Implementar um servidor para reconstrução de imagens:
				</p>
				<ul>
					<li>Receber os dados para reconstrução;</li>
					<li>Carregar o modelo de reconstrução de acordo com os parâmetros recebidos;</li>
					<li>Executar o algoritmo de reconstrução;</li>
					<li>Executar até que o erro (ϵ) seja menor do que 1e10-4 .</li>
					<li>Salvar o resultado.</li>
				</ul>
			</div>
		</div>
	)	
}

export default Help;