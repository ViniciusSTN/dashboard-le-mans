import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

# motor carros
cursor.execute("SELECT id_motor, potencia_motor, foto_carro, ano FROM vencedores")
motor_carros = cursor.fetchall()

cursor.execute("SELECT id, nome FROM motores")
motores_table = cursor.fetchall()

id_motores = []
nome_motores = []
for motor in motores_table:
   id, name = motor
   id_motores.append(id)
   nome_motores.append(name)

motor_tratar = []
potencia_motores = []
foto_carros = []
anos = []

for tupla in motor_carros:
    id_motor, potencia_motor, foto_carro, ano = tupla
    # Substituir o id_motor pelo nome correspondente
    if id_motor in id_motores:
        motor_index = id_motores.index(id_motor)
        motor_nome = nome_motores[motor_index]
        motor_tratar.append(motor_nome)
    else:
        # Caso o id_motor não seja encontrado, você pode tomar uma ação padrão
        motor_tratar.append("Motor Desconhecido")

    potencia_motores.append(potencia_motor)
    foto_carros.append(foto_carro)
    anos.append(ano)


min_potencia = min(potencia_motores)
max_potencia = max(potencia_motores)
# estatistica descritiva
from statistics import mean, pstdev

media_potencia = round(mean(potencia_motores), 2)
dp_potencia = round(pstdev(potencia_motores), 2)
cv_potencia = round((dp_potencia / media_potencia) * 100, 2)
      
dados_motores = []
for i in range(len(motor_tratar)):
    dado = {
        'motores': motor_tratar[i],
        'potencia motores': potencia_motores[i],
        'imagem carro': foto_carros[i],
        'ano': anos[i],
    }
    dados_motores.append(dado)


dado_estatisticos = [{
    'media potencia': media_potencia,
    'dp potencia': dp_potencia,
    'cv potencia': cv_potencia,
}]

min_max_potencia = [{
    'minima potencia': min_potencia,
    'maxima potencia': max_potencia
}]

potencia_minima_e_maxima = pd.DataFrame(min_max_potencia)
dados_motor = pd.DataFrame(dados_motores)
dados_estatisticos_motor = pd.DataFrame(dado_estatisticos)
conn.close()
