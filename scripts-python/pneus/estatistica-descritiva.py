import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# pneus
cursor.execute("SELECT participacoes, vitorias FROM pneus")
pneus = cursor.fetchall()

participacoes = []
vitorias = []

for tupla in pneus:
  participacoes.append(tupla[0])
  vitorias.append(tupla[1])

# estatistica descritiva
from statistics import mean, pstdev

media_participacoes = round(mean(participacoes), 2)
dp_participacoes = round(pstdev(participacoes), 2)
cv_participacoes = round((dp_participacoes / media_participacoes) * 100, 2)

media_vitorias = round(mean(vitorias), 2)
dp_vitorias = round(pstdev(vitorias), 2)
cv_vitorias = round((dp_vitorias / media_vitorias) * 100, 2)

dados_geral = [{
  'media participacoes': media_participacoes,
  'dp participacoes': dp_participacoes,
  'cv participacoes': cv_participacoes,
  'media vitorias': media_vitorias,
  'dp vitorias': dp_vitorias,
  'cv vitorias': cv_vitorias,
}]

pneus_geral = pd.DataFrame(dados_geral)

conn.close()
