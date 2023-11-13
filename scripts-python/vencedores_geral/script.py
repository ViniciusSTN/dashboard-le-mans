import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\vinic\\Desktop\\le-mans\\teste\\le-mans.db')
cursor = conn.cursor()

# voltas_mais_rapidas
cursor.execute("SELECT * FROM voltas_mais_rapidas")
resultados = cursor.fetchall()
voltas_mais_rapidas = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# pilotos
cursor.execute("SELECT * FROM pilotos")
resultados = cursor.fetchall()
pilotos = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# circuitos
cursor.execute("SELECT * FROM circuitos")
resultados = cursor.fetchall()
circuitos = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# construtores
cursor.execute("SELECT * FROM construtores")
resultados = cursor.fetchall()
construtores = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# motores
cursor.execute("SELECT * FROM motores")
resultados = cursor.fetchall()
motores = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# pneus
cursor.execute("SELECT * FROM pneus")
resultados = cursor.fetchall()
pneus = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

# vencedores
cursor.execute("SELECT * FROM vencedores")
resultados = cursor.fetchall()
vencedores = pd.DataFrame(resultados, columns=[col[0] for col in cursor.description])

conn.close()
