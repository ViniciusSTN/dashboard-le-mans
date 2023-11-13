import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

# Recuperar dados do banco de dados
cursor.execute("SELECT carro, ano, id FROM vencedores")
carros_vitorias = cursor.fetchall()

# Criar um DataFrame
carros_df = pd.DataFrame(carros_vitorias, columns=["Carro", "Ano", "id"])

# Adicionar a coluna 'Vitorias' ao DataFrame
carros_df['Vitorias'] = carros_df.groupby('Carro')['Carro'].transform('count')

# Estatísticas descritivas
resultados = []
from statistics import mean, pstdev
for index, row in carros_df.iterrows():
    carro = row['Carro']
    ano = row['Ano']
    id_anos = row['id']

    cursor.execute("SELECT voltas, distancia FROM vencedores WHERE carro = ?", (carro,))
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
        'Carro': carro,
        'Ano': ano,
        'Id': id_anos,
        'Vitorias': carros_df['Vitorias'].iloc[index],
        'Média de Voltas': media_voltas,
        'DP de Voltas': dp_p_voltas,
        'CV de Voltas': cv_voltas,
        'Média de Distância': media_distancia,
        'DP de Distância': dp_p_distancia,
        'CV de Distância': cv_distancia,
    })

conn.close()

# Criar um DataFrame com os resultados
carros_df = pd.DataFrame(resultados)

# Exibir o DataFrame
print(carros_df)
