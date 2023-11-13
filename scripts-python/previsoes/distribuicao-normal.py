import sqlite3
import pandas as pd
import scipy.stats as stats
from statistics import mean, pstdev

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# pneus
cursor.execute("SELECT distancia FROM circuitos")
dados_brutos = cursor.fetchall()

distancias = []

for tupla in dados_brutos:
    distancias.append(tupla[0])

media = round(mean(distancias), 2)
dp = round(pstdev(distancias), 2)

z = 0 - round(((14500 - media) / dp), 2)

probabilidade = round(stats.norm.cdf(z) * 100, 2)

dados = [{
    'Média da distancia': media,
    'DP da distancia': dp,
    'Resultado': probabilidade
}]

distribuicao_normal = pd.DataFrame(dados)

conn.close()
