import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT tempo, velocidade_media FROM voltas_mais_rapidas WHERE ano BETWEEN 1932 AND 1955")
regressao_ = cursor.fetchall()

print(regressao_)
tempo_volta = []
velocidade = []

for tupla in regressao_:
    tempo, velocidade_media = tupla
    tempo_volta.append(tempo)
    velocidade.append(velocidade_media)


calculo_regressao = 330.56 + (150 * (-0.00056))

calculo_regressao_transformar = 330476

minutos, milissegundos = divmod(calculo_regressao_transformar, 60000)
segundos, milissegundos = divmod(milissegundos, 1000)

tempo_formatado = f'{minutos}:{segundos}.{milissegundos}'
tempo_formatados = []
for valor_em_milissegundos in tempo_volta:
    minutos, milissegundos = divmod(valor_em_milissegundos, 60000)
    segundos, milissegundos = divmod(milissegundos, 1000)
    tempo_formatado = f'{minutos}:{segundos}.{milissegundos}'
    tempo_formatados.append(tempo_formatado)




grafico_regressao = []
for i in range(len(regressao_)):
    dado = {
        'tempos formatados': tempo_formatados[i],
        'tempo voltas(X)': tempo_volta[i],
        'velocidade': velocidade[i],
    }
    grafico_regressao.append(dado)
print(grafico_regressao)
dados = [{
    'R multiplo': 97.82,
    'F de significação': 0.00000009,
    'coeficiente X': -0.00056,
    'coeficiente Interseção': 330.56,
    'Valor-p(X)': 0.00000003,
    'tempo sem formatar': calculo_regressao,
    'tempo volta': tempo_formatado
}]

grafico_para_regressao = pd.DataFrame(grafico_regressao)
regressao = pd.DataFrame(dados)
conn.close()


