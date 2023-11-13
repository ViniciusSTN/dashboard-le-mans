import sqlite3
import pandas as pd

from statistics import mean, pstdev
# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()
resultados = []
cursor.execute("SELECT voltas, distancia FROM vencedores")
voltas_e_distancia = cursor.fetchall()

voltas = [voltas[0] for voltas in voltas_e_distancia]
distancia = [distancia[1] for distancia in voltas_e_distancia]

if voltas: 
    media_voltas = round(mean(voltas), 2)
    dp_p_voltas = round(pstdev(voltas), 2)
    cv_voltas = round((dp_p_voltas / media_voltas) * 100, 2)
else: 
    media_voltas = dp_p_voltas = cv_voltas = 0.0

if distancia:
    media_distancia = round(mean(distancia), 2)
    dp_p_distancia = round(pstdev(distancia), 2)
    cv_distancia = round((dp_p_distancia / media_distancia) * 100, 2)
else:
    media_distancia = dp_p_distancia = cv_distancia = 0.0

resultados.append({
    'Média de Voltas': media_voltas,
    'DP de Voltas': dp_p_voltas,
    'CV de Voltas': cv_voltas,
    'Média de Distância': media_distancia,
    'DP de Distância': dp_p_distancia,
    'CV de Distância': cv_distancia,
    })

print(resultados)