import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

def dados_tratados(dados):
  dado_tratado = []

  for tupla in dados:
    nome, participacoes, vitorias = tupla

    dado = {
      'nome': nome,
      'participacoes': participacoes,
      'vitorias': vitorias,
    }
    dado_tratado.append(dado)

  return dado_tratado

# top 5 vitorias
cursor.execute("SELECT nome, participacoes, vitorias FROM pneus ORDER BY vitorias desc LIMIT 5")
top5_vitorias_bruto = cursor.fetchall()

top5_vitorias = dados_tratados(top5_vitorias_bruto)
top_vitorias_pneus = pd.DataFrame(top5_vitorias)

# top 5 participacoes
cursor.execute("SELECT nome, participacoes, vitorias FROM pneus ORDER BY participacoes desc LIMIT 5")
top5_participacoes_bruto = cursor.fetchall()

top5_participacoes = dados_tratados(top5_participacoes_bruto)
print(top5_participacoes)
top_participacoes_pneus = pd.DataFrame(top5_participacoes)
