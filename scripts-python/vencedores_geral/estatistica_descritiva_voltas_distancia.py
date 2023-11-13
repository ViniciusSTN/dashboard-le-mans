import sqlite3
import pandas as pd

conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT voltas, distancia FROM vencedores")
descritiva = cursor.fetchall()


voltas_sem_somar = []
distancia_sem_somar = []

for tupla in descritiva:
    voltas, distancia = tupla
    voltas_sem_somar.append(voltas)
    distancia_sem_somar.append(distancia)

voltas_somadas_sem_formatar = sum(voltas_sem_somar)

voltas_somadas = [voltas_somadas_sem_formatar]


distancia_somadas_sem_formatar = sum(distancia_sem_somar)

distancia_somadas = [distancia_somadas_sem_formatar]


from statistics import mean, pstdev

media_voltas = round((voltas_somadas_sem_formatar / 91), 2)
dp_voltas = round(pstdev(voltas_sem_somar), 2)
cv_voltas = round((dp_voltas / media_voltas)* 100, 2)

media_distancia = round((distancia_somadas_sem_formatar / 91), 2)
dp_distancia = round(pstdev(distancia_sem_somar), 2)
cv_distancia = round((dp_distancia / media_distancia)* 100, 2)


dados_geral = [{
  'media voltas': media_voltas,
  'dp voltas': dp_voltas,
  'cv ': cv_voltas,
  'media distancia': media_distancia,
  'dp distancia': dp_distancia,
  'cv distancia': cv_distancia,
}]

dados_estatisticos_voltas_distancia = pd.DataFrame(dados_geral)
conn.close()