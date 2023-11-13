import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\teste\\le-mans.db')
cursor = conn.cursor()

# carro
cursor.execute("SELECT voltas, distancia FROM vencedores")
quantitativos = cursor.fetchall()

for dados in quantitativos:
  