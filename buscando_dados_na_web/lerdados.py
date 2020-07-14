import investpy as inv
import pandas as pd

# fazendo uma listagem de todas as ações no banco de dados
""" acoes_br = inv.get_stocks('brazil')
print(acoes_br) """

acoes_br = inv.get_stocks_list('brazil')
print(acoes_br)

# buscando uma descrição de uma ação
""" acoes_br = inv.get_stock_company_profile('USIM5', country='brazil')
print(acoes_br) """

# baixando a contação hitorica
""" usim5 = inv.get_stock_historical_data('USIM5', country='brazil', from_date='01/01/1900', to_date='11/07/2020')
print(usim5) #posso acrecentar ['nome da coluna'] para exibir so a conluna """