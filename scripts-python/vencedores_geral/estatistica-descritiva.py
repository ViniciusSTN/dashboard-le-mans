import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# circuito
cursor.execute("SELECT distancia, velocidade_media, url_circuito, ano_implementado FROM circuitos")
circuito = cursor.fetchall()
distancias = []
velocidades_medias = []
urls_circuitos = []
ano_implementado = []

for tupla in circuito:
  distancia, velocidade_media, url, ano = tupla
  distancias.append(distancia)
  velocidades_medias.append(velocidade_media)
  urls_circuitos.append(url)
  ano_implementado.append(ano)

# estatistica descritiva
from statistics import mean, pstdev

media_distancias = round(mean(distancias), 2)
dp_distancias = round(pstdev(distancias), 2)
cv_distancias = round((dp_distancias / media_distancias) * 100, 2)

media_velocidades = round(mean(velocidades_medias), 2)
dp_velocidades = round(pstdev(velocidades_medias), 2)
cv_velocidades = round((dp_velocidades / media_velocidades) * 100, 2)

dados_cada_circuito = []

for i in range(len(distancias)):
  dado = {
    'distancia': distancias[i],
    'velocidade media': velocidades_medias[i],
    'imagem': urls_circuitos[i],
    'ano implementado': ano_implementado[i]
  }
  dados_cada_circuito.append(dado)

dados_geral = [{
  'media_distancias': media_distancias,
  'dp distancias': dp_distancias,
  'cv distancias': cv_distancias,
  'media velocidades': media_velocidades,
  'dp velocidades': dp_velocidades,
  'cv velocidades': cv_velocidades
}]
circuitos = pd.DataFrame(dados_cada_circuito)
circuitos_geral = pd.DataFrame(dados_geral)
conn.close()
