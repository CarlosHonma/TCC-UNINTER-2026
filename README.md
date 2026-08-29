# 🌡️ Sistema Embarcado para Monitoramento de Temperatura e Umidade

Projeto desenvolvido como Trabalho de Conclusão de Curso de **Engenharia da Computação da UNINTER**, em 2026.

O sistema realiza o monitoramento de temperatura e umidade utilizando o microcontrolador **PIC16F877A** e o sensor **DHT11**. Os dados coletados são transmitidos ao computador por comunicação serial **UART**, armazenados em banco de dados **SQLite** e apresentados graficamente por uma aplicação desenvolvida em **Python**.

## 🎯 Objetivo

Desenvolver uma solução embarcada de baixo custo capaz de:

- Monitorar temperatura e umidade;
- Processar os dados com o PIC16F877A;
- Transmitir informações por UART;
- Armazenar as medições em SQLite;
- Exibir os dados por meio de gráficos.

## 🔧 Tecnologias

### Hardware

- PIC16F877A
- Sensor DHT11
- Placa PIC DIP40
- PICkit 3
- Conversor USB/Serial

### Software

- Linguagem C
- MPLAB X IDE
- Compilador XC8
- Python
- SQLite
- Pandas
- Matplotlib
- PySerial

## ⚙️ Funcionamento

```text
DHT11
  ↓
PIC16F877A
  ↓
UART
  ↓
USB/Serial
  ↓
Python
  ├── SQLite
  └── Matplotlib
```

O sensor realiza a coleta das variáveis ambientais, enquanto o microcontrolador processa e envia os dados ao computador. A aplicação Python recebe as informações, realiza o armazenamento e permite sua visualização gráfica.

## 📂 Estrutura do Projeto

```text
TCC-UNINTER-2026/
│
├── firmware/
│   └── PIC16F877A/
│
├── python/
│   ├── monitor_dht11.py
│   ├── interface_grafica.py
│   ├── requirements.txt
│   └── dados_sensor.db
│
├── interface-grafica/
├── README.md
└── .gitignore
```

A pasta `interface-grafica/` contém uma versão web experimental desenvolvida como possibilidade de expansão do projeto.

## 🚀 Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aquisição dos dados:

```bash
python monitor_dht11.py
```

Em outro terminal, execute a interface gráfica:

```bash
python interface_grafica.py
```

A comunicação serial utilizada durante o desenvolvimento foi configurada em **9600 baud**, utilizando a porta **COM5**.

## 👨‍💻 Autor

**Carlos Eduardo Eiti Honma Antunes**  
Engenharia da Computação — UNINTER  
2026

## 🔗 Repositório

https://github.com/CarlosHonma/TCC-UNINTER-2026
