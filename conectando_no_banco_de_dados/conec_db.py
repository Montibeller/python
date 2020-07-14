import sqlite3
import time
import datetime

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

def create_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS dados(id interger, unix real, keyword text, datestamp text, value real)')

create_tabela()

data_id = 4
keyword = 'Pythin is awesome!'
value = 4

def dataentry():
   """  c.execute("INSERT INTO dados VALUES(1, 13.56, 'Python Sentiment', '2013-04-14 10:09:41', 5)")
    c.execute("INSERT INTO dados VALUES(2, 133625757.56, 'Python Sentiment', '2013-04-14 10:09:41', 6)")
    c.execute("INSERT INTO dados VALUES(3, 132346236.56, 'Python Sentiment', '2013-04-14 10:09:41', 4)")
    connection.commit() """
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H-%M-%S'))

    c.execute('INSET INTO dados (id, unix, keyword, datestamp, value') 


dataentry()
