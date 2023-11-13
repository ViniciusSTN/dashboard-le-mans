import sqlite3
import pandas as pd

conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT nome, participacoes FROM construtores")
construtores = cursor.fetchall()

query_participacoes = """
    SELECT nome, participacoes FROM construtores WHERE participacoes >= 100;
"""
construtores_com_mais_parti = pd.read_sql_query(query_participacoes, conn)
print(construtores_com_mais_parti)
query_vitorias = """
    SELECT nome, participacoes, vitorias FROM construtores WHERE vitorias >= 5;
"""
construtores_com_mais_vitorias = pd.read_sql_query(query_vitorias, conn)
conn.close()