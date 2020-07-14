#import investpy as inv
import sqlite3


connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS acoes(\
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
        cod TEXT UNIQUE NOT NULL, \
        nome TEXT NOT NULL)')
create_tabela()

#acoes_br = inv.get_stocks_list('brazil')