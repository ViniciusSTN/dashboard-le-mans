import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

# vencedores
cursor.execute("SELECT id_motor, potencia_motor, foto_carro FROM vencedores")
carro = cursor.fetchall()

motores = []
potencia_motores = []
foto_carros = []

for tupla in carro:
  id_motor, potencia_motor, foto_carro = tupla
  motores.append(id_motor)
  potencia_motores.append(potencia_motor)
  foto_carros.append(foto_carro)

# estatistica descritiva
from statistics import mean, pstdev




