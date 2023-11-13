import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# motores e carros
cursor.execute("SELECT v.carro, v.foto_carro, m.nome FROM motores as m LEFT JOIN vencedores as v ON m.id = v.id_motor GROUP BY v.carro")
motores_carros = cursor.fetchall()

dados = []

for tupla in motores_carros:
  dado = {
    'nome carro': tupla[0],
    'foto carro': tupla[1],
    'nome motor': tupla[2],
  }
  dados.append(dado)

motores_geral = pd.DataFrame(dados)

conn.close()
