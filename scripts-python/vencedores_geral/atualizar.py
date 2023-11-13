import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT velocidade_media, carro FROM voltas_mais_rapidas WHERE velocidade_media = (SELECT MAX(velocidade_media) FROM voltas_mais_rapidas)")
velocidade = cursor.fetchall()


velocidade_, carro = velocidade[0]

saida_ = [{
    'velocidade média': velocidade_,
    'carro': carro
}]

velocidade_media = pd.DataFrame(saida_)