import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

# carro
cursor.execute("SELECT ano, carro, voltas, distancia FROM vencedores")
carros = cursor.fetchall()

carros_geral = pd.DataFrame(carros)
