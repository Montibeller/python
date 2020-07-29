import numpy as np
import pandas as pd
import string
import warnings
warnings.filterwarnings('ignore')
from urllib.request import Request, urlopen

req = Request('http://www.fundamentus.com.br/resultado.php', headers={'User-Agent': 'XYZ/3.0'})
df = pd.read_html(urlopen(req, timeout=10).read(), decimal=',', thousands='.')[0]

for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
    df[coluna] = df[coluna].str.replace('.', '')
    df[coluna] = df[coluna].str.replace(',', '.')
    df[coluna] = df[coluna].str.rstrip('%').astype('float') / 100

# print(df)

''' ANALIZANDO DADOS '''

df = df[df['Liq.2meses'] > 1000000]

ranking = pd.DataFrame()
ranking['pos'] = range(1,151)
ranking['EV/EBIT'] = df[ df['EV/EBIT'] > 0 ].sort_values(by=['EV/EBIT'])['Papel'][:150].values
ranking['ROIC'] = df.sort_values(by=['ROIC'], ascending=False)['Papel'][:150].values

#print(ranking)

a = ranking.pivot_table(columns='EV/EBIT', values='pos')
b = ranking.pivot_table(columns='ROIC', values='pos')
t = pd.concat([a,b])

#print(t)

rank = t.dropna(axis=1).sum()

print(rank.sort_values()[:15])