import serial

# ajuste a COM conforme seu computador
pic = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=1
)

def ler_serial():
    linha = pic.readline().decode().strip()
    return linha