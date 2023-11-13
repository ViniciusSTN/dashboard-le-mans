import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\bd\\le-mans.db')
# conn = sqlite3.connect('/home/vinicius/Downloads/le-mans.db')
cursor = conn.cursor()

# pneus
cursor.execute("SELECT nome, participacoes, vitorias FROM pneus")
pneus = cursor.fetchall()

dados_pneus = []
vitorias = []
participacoes = []

for tupla in pneus:
  dado = {
    'nome': tupla[0],
    'participacoes': tupla[1],
    'vitorias': tupla[2],
  }
  dados_pneus.append(dado)
  participacoes.append(tupla[1])
  vitorias.append(tupla[2])


maior_vitoria = max(vitorias)
menor_vitoria = min(vitorias)

maior_participacoes = max(participacoes)
menor_participacoes = min(participacoes)

maior_menor = [{
  'maior vitoria': maior_vitoria,
  'menor vitoria': menor_vitoria,
  'maior participacoes': maior_participacoes,
  'menor participacoes': menor_participacoes,
}]

todos_pneus = pd.DataFrame(dados_pneus)
maior_menor_pneus = pd.DataFrame(maior_menor)

conn.close()
