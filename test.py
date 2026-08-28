import serial
import time

try:

    porta = serial.Serial(
        port='COM5',
        baudrate=9600,
        timeout=2
    )

    time.sleep(2)

    print("Conectado com sucesso!\n")

    while True:

        if porta.in_waiting > 0:

            dado = porta.readline().decode(
                'utf-8',
                errors='ignore'
            ).strip()

            if dado:
                print(dado)

except Exception as erro:

    print("Erro:")
    print(erro)