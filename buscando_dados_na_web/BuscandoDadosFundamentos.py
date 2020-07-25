import numpy as np
import pandas as pd
import string
import warnings
warnings.filterwarnings('ignore')
from urllib.request import Request, urlopen

req = Request('http://www.fundamentus.com.br/resultado.php', headers={'User-Agent': 'XYZ/3.0'})
df = pd.read_html(urlopen(req, timeout=10).read())[0]

print(df)