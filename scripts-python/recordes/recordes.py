# volta mais rapida ja registrada X
# velocidade media mais alta ja registradax
# maior distancia percorrida ja registradax
# maior quantidade de vitorias consecutivas de pilotosx
# maior quantidade de vitorias consecutivas de construtoresx

import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT carro, tempo FROM voltas_mais_rapidas WHERE tempo = (SELECT MIN(tempo) FROM voltas_mais_rapidas) ")
volta_mais_rapida = cursor.fetchall()

carro, tempo_volta = volta_mais_rapida[0]

minutos, milissegundos = divmod(tempo_volta, 60000)
segundos, milissegundos = divmod(milissegundos, 1000)

# Junte os valores em uma única variável
tempo_formatado = f'{minutos}:{segundos}.{milissegundos}'

saida = [{
    'carro': carro,
    'tempo': tempo_formatado
}]

volta_mais_rapida_ = pd.DataFrame(saida)

cursor.execute("SELECT velocidade_media, carro FROM voltas_mais_rapidas WHERE velocidade_media = (SELECT MAX(velocidade_media) FROM voltas_mais_rapidas)")
velocidade = cursor.fetchall()


velocidade_, carro = velocidade[0]

saida_ = [{
    'velocidade média': velocidade_,
    'carro': carro
}]

velocidade_media = pd.DataFrame(saida_)

cursor.execute("SELECT carro, distancia, voltas FROM vencedores WHERE distancia = (SELECT MAX(distancia) FROM vencedores) ")
distancia_percorrida = cursor.fetchall()

carro, distancia, voltas = distancia_percorrida[0]
saida = [{
    'carro': carro,
    'distancia': distancia,
    'voltas': voltas
}]

distancia_percorrida_recorde = pd.DataFrame(saida)

query = """
WITH Sequencias AS (
    SELECT
        id_piloto,
        LAG(id_piloto) OVER (ORDER BY id_piloto) AS prev_id,
        LEAD(id_piloto) OVER (ORDER BY id_piloto) AS next_id
    FROM pilotos_vencedores
)

SELECT id_piloto, COUNT(*) AS contagem
FROM Sequencias
WHERE id_piloto = prev_id AND id_piloto = next_id AND id_piloto <> 42
GROUP BY id_piloto
ORDER BY contagem DESC
LIMIT 3;
"""
pilotos = pd.read_sql_query(query, conn)


cursor.execute("SELECT nome, id FROM pilotos WHERE id = 25 OR id = 181 OR id = 79")
pilotos_ = cursor.fetchall()

pilotos_com_mais_vitorias_consecutivas = pd.DataFrame(pilotos_, columns=['Nome', 'id'])
contagem = pd.DataFrame({
    'id': [25, 181, 79],
    'contagem': [6, 3, 3]
})

# Mesclar os DataFrames com base na coluna 'id' em comum
resultado = pilotos_com_mais_vitorias_consecutivas.merge(contagem, on='id')


carros = ['porsche', 'Ferrari', 'Audi' ]
vitorias = ['7', '6', '5']

dados_vito = []
for i in range(len(carros)):
    dado = {
        'carro': carros[i],
        'vitorias': vitorias[i],
    }
    dados_vito.append(dado)

vitorias_consecutivas = pd.DataFrame(dados_vito)

conn.close()


query = """
WITH Sequencias AS (
    SELECT
        equipe,
        LAG(equipe) OVER (ORDER BY equipe) AS prev_equipe,
        LEAD(equipe) OVER (ORDER BY equipe) AS next_equipe
    FROM pilotos_vencedores
)

SELECT id_piloto, COUNT(*) AS contagem
FROM Sequencias
WHERE id_piloto = prev_id AND id_piloto = next_id AND id_piloto <> 42
GROUP BY id_piloto
ORDER BY contagem DESC
LIMIT 3;
"""
pilotos = pd.read_sql_query(query, conn)