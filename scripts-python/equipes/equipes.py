import sqlite3
import pandas as pd

conn = sqlite3.connect('C:\\Users\\muril\\Downloads\\le-mans.db')
cursor = conn.cursor()

cursor.execute("SELECT equipe FROM vencedores")
equipes = cursor.fetchall()

query = """
SELECT equipe, COUNT(*) as total
FROM vencedores
WHERE equipe <> 'Sem designação'
GROUP BY equipe
ORDER BY total DESC
LIMIT 6;
"""

equipes_formatadas = pd.read_sql_query(query, conn)




