import sqlite3

# cria conexão
conn = sqlite3.connect("sensores.db")
cursor = conn.cursor()

# cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    horario TEXT,
    temperatura REAL,
    umidade REAL
)
""")

conn.commit()