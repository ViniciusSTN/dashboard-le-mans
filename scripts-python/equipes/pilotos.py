import sqlite3
import pandas as pd

conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute('SELECT id_edicao, id_piloto FROM pilotos_vencedores')
pilotos_tratar = cursor.fetchall()
# selecionar dados apenas dos pilotos que ja venceram le mans
cursor.execute("SELECT id, vitorias, nome, participacoes FROM pilotos WHERE vitorias > 0")
pilotos_vitorias = cursor.fetchall()
# --------------------------------------------------------------
id_pilotos_ori = []
nome_pilotos = []
participacoes_pilotos = []
vitorias_pilotos = []
for pilots in pilotos_vitorias:
    id, vitorias, nome, participacoes = pilots
    nome_pilotos.append(nome)
    participacoes_pilotos.append(participacoes)
    id_pilotos_ori.append(id)
    vitorias_pilotos.append(vitorias)

cursor.execute("SELECT id, vitorias, nome, participacoes FROM pilotos WHERE vitorias > 4")
vitorias_piloto = cursor.fetchall()

nome_ = []
participacoes_ = []
id_ = []
vitorias_ = []
for tupla in vitorias_piloto:
    id, vitorias, nome, participacoes = tupla
    nome_.append(nome)
    participacoes_.append(participacoes)
    id_.append(id)
    vitorias_.append(vitorias)

maiores_vencedores = []
for i in range(len(vitorias_piloto)):
    dados = {
        'id': id_[i],
        'nome': nome_[i],
        'participações': participacoes_[i],
        'vitorias': vitorias_[i],
	}
    maiores_vencedores.append(dados)
# ----------------------------------------------------------------------------
from statistics import mean, pstdev

media_vitorias = round(mean(vitorias_pilotos), 2)
dp_vitorias = round(pstdev(vitorias_pilotos), 2)
cv_potencia = round((dp_vitorias / media_vitorias) * 100, 2)
# -----------------------------------------------------------------------------

query_pilotos_mais_vitoriosos = """
	SELECT id, nome, vitorias, participacoes FROM pilotos WHERE vitorias >= 5;
"""
pilotos_mais_vitorioso = pd.read_sql_query(query_pilotos_mais_vitoriosos, conn)

query_pilotos = """
    SELECT id, nome, vitorias, participacoes FROM pilotos WHERE participacoes >= 15;
"""
pilotos_com_mais_aproveitamento = pd.read_sql_query(query_pilotos, conn)

# ----------------------------------------------------------------------------
vitorias_piloto_ = []
for i in range(len(pilotos_com_mais_aproveitamento)):
    dado = {
	  	'nome piloto': nome_pilotos[i],
    	'participações': participacoes_pilotos[i],
    	'vitorias': vitorias_pilotos[i],
   	 	'id piloto': id_pilotos_ori[i],
  	}
    vitorias_piloto_.append(dado)

aproveitamento = []
for piloto in vitorias_piloto_:
	dado = {
		'nome_piloto': piloto['nome piloto'],
		'porcentagem de aproveitamento': round((piloto['vitorias'] / piloto['participações']) * 100, 2),
        'vitorias': piloto['vitorias'],
		'id piloto': piloto['id piloto'],
        'participações': piloto['participações']
	}
	aproveitamento.append(dado)

melhores_aproveitamentos = []
for piloto in aproveitamento:
    if piloto['porcentagem de aproveitamento'] >= 30:
      dado = {
		'nome': piloto['nome_piloto'],
        'participações': piloto['participações'],
        'vitorias': piloto['vitorias'],
        'aproveitamento': piloto['porcentagem de aproveitamento'],
		'id piloto': piloto['id piloto'],
      }
      melhores_aproveitamentos.append(dado)

# ----------------------------------------------------------------------------

dados_estatisticos = [{
	'media de vitorias': media_vitorias,
	'dp de vitoria': dp_vitorias,
    'cv de vitorias': cv_potencia,
}]

# ----------------------------------------------------------------------------

melhores_aproveitamentos_pilotos = pd.DataFrame(melhores_aproveitamentos)
vitorias_por_pilotos = pd.DataFrame(vitorias_piloto)
dados_estatisticos_velocidade = pd.DataFrame(dados_estatisticos)
maiores_vencedores_ = pd.DataFrame(maiores_vencedores)
conn.close()