#import investpy as inv
import sqlite3


connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_tabela_acoes():
    c.execute('''CREATE TABLE IF NOT EXISTS acoes(
			        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			        cod TEXT UNIQUE NOT NULL,
			        nome TEXT NOT NULL)''')
create_tabela_acoes()

def create_tabela_cotacoes():
	c.execute('''CREATE TABLE IF NOT EXISTS cotacoes(
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					acao INTEGER,
					abertura REAL,
					fechamento REAL,
					maxima REAL,
					minima REAL,
					volume REAL,)''')
create_tabela_cotacoes()

#acoes_br = inv.get_stocks_list('brazil')