from serial_com import ler_serial
from database import conn, cursor
from datetime import datetime

while True:
    try:
        linha = ler_serial()

        # verifica se recebeu algo
        if linha:
            print("Recebido:", linha)

            # separa temperatura e umidade
            temperatura, umidade = linha.split(",")
            temperatura = float(temperatura)
            umidade = float(umidade)
            horario = datetime.now()

            # salva no banco
            cursor.execute("""
            INSERT INTO leituras
            (horario, temperatura, umidade)
            VALUES (?, ?, ?)
            """, (
                str(horario),
                temperatura,
                umidade
            ))

            conn.commit()

            print("Dados salvos!")

    except Exception as erro:

        print("Erro:", erro)