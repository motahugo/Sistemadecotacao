import requests
import json
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Sistema de Cotação de Moedas")

mensagem = tk.Label(text='Selecione a Moeda \n' 'Clique em Buscar', bg='#191970',fg='white', height=3,width=30)
mensagem.grid()


dados = requests.get('https://economia.awesomeapi.com.br/json/all')
dados_dic = dados.json()

moedas = list(dados_dic.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=3, column=0)


def buscar_cotacao():
    moeda_preenchida  = moeda.get()
    cotacao_moeda = dados_dic.get(moeda_preenchida)['bid']
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=6, column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'



botao = tk.Button(text="Buscar Cotação", command= buscar_cotacao)
botao.grid(row=4, column=0)



janela.mainloop()