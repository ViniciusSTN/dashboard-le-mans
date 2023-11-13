import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# motores e carros
cursor.execute("SELECT vitorias, participacoes, voltas_mais_rapidas FROM motores")
motores_carros = cursor.fetchall()

vitorias = []
participacoes = []
voltas_mais_rapidas = []

for tupla in motores_carros:
    vitorias.append(tupla[0])
    participacoes.append(tupla[1])
    voltas_mais_rapidas.append(tupla[2])


from statistics import mean, pstdev

media_vitorias = round(mean(vitorias), 2)
dp_vitorias = round(pstdev(vitorias), 2)
cv_vitorias = round((dp_vitorias / media_vitorias) * 100, 2)

media_participacoes = round(mean(participacoes), 2)
dp_participacoes = round(pstdev(participacoes), 2)
cv_participacoes = round((dp_participacoes / media_participacoes) * 100, 2)

media_voltas_mais_rapidas = round(mean(voltas_mais_rapidas), 2)
dp_voltas_mais_rapidas = round(pstdev(voltas_mais_rapidas), 2)
cv_voltas_mais_rapidas = round((dp_voltas_mais_rapidas / media_voltas_mais_rapidas) * 100, 2)

dados = [{
    'media vitorias': media_vitorias,
    'dp vitorias': dp_vitorias,
    'cv vitorias': cv_vitorias,
    'media participacoes': media_participacoes,
    'dp participacoes': dp_participacoes,
    'cv participacoes': cv_participacoes,
    'media voltas mais rapidas': media_voltas_mais_rapidas,
    'dp voltas mais rapidas': dp_voltas_mais_rapidas,
    'cv voltas mais rapidas': cv_voltas_mais_rapidas,
}]

estatistica_motores = pd.DataFrame(dados)

conn.close()