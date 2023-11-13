import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()



query = """
WITH Sequencias AS (
    SELECT
        equipe,
        LAG(equipe) OVER (ORDER BY equipe) AS prev_equipe,
        LEAD(equipe) OVER (ORDER BY equipe) AS next_equipe
    FROM vencedores
)

SELECT equipe, COUNT(*) AS contagem
FROM Sequencias
WHERE equipe = prev_equipe AND equipe = next_equipe AND equipe <> 'Sem designação'
GROUP BY equipe
ORDER BY contagem DESC
LIMIT 5;
"""
equipes_mais_vencedoras = pd.read_sql_query(query, conn)

