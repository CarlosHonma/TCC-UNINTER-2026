import serial
import sqlite3
import re
from datetime import datetime
import time

# CONFIGURAÇÃO SERIAL

PORTA = 'COM5'
BAUDRATE = 9600

# BANCO DE DADOS

conexao = sqlite3.connect("dados_sensor.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora TEXT,
    temperatura INTEGER,
    umidade INTEGER
)
""")

conexao.commit()

# SERIAL

try:
    serial_pic = serial.Serial(
        PORTA,
        BAUDRATE,
        timeout=2
    )

    time.sleep(2)

    print("Conectado ao PIC!\n")

    temperatura = None
    umidade = None

    while True:
        if serial_pic.in_waiting > 0:
            dado = serial_pic.readline().decode(
                'utf-8',
                errors='ignore'
            ).strip()
            print(dado)

            # TEMPERATURA
            
            temp_match = re.search(r'T:(\d+)C', dado)
            if temp_match:
                temperatura = int(temp_match.group(1))
            
            # UMIDADE

            umid_match = re.search(r'U:(\d+)%', dado)
            if umid_match:
                umidade = int(umid_match.group(1))
            
            # SALVA NO BANCO

            if temperatura is not None and umidade is not None:
                agora = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                cursor.execute("""
                INSERT INTO leituras (
                    data_hora,
                    temperatura,
                    umidade
                )
                VALUES (?, ?, ?)
                """, (
                    agora,
                    temperatura,
                    umidade
                ))

                conexao.commit()

                print("\nSALVO NO BANCO:")
                print(
                    f"Temperatura: {temperatura}°C"
                )

                print(
                    f"Umidade: {umidade}%"
                )

                print(
                    f"Horario: {agora}\n"
                )

                # evita salvar duplicado
                temperatura = None
                umidade = None
except Exception as erro:
    print("Erro:")
    print(erro)