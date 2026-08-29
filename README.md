# 🌡️ Sistema Embarcado para Monitoramento de Temperatura e Umidade

Projeto desenvolvido como Trabalho de Conclusão de Curso de **Engenharia da Computação da UNINTER**, em 2026.

O sistema realiza o monitoramento de temperatura e umidade utilizando o microcontrolador **PIC16F877A** e o sensor **DHT11**. Os dados coletados são transmitidos ao computador por comunicação serial **UART**, armazenados em banco de dados **SQLite** e apresentados graficamente por uma aplicação desenvolvida em **Python**.

## 🎯 Objetivo

Desenvolver uma solução embarcada de baixo custo capaz de:

- Monitorar temperatura e umidade;
- Processar os dados utilizando o PIC16F877A;
- Transmitir as informações por UART;
- Armazenar as medições em SQLite;
- Apresentar os dados por meio de gráficos;
- Manter um histórico das medições realizadas.

## 🔧 Tecnologias Utilizadas

### Hardware

- Microcontrolador PIC16F877A
- Sensor DHT11
- Placa PIC DIP40
- Cristal de 20 MHz
- PICkit 3
- Conversor USB/Serial

### Software

- Linguagem C
- MPLAB X IDE
- Compilador XC8
- Python
- PySerial
- SQLite
- Pandas
- Matplotlib
- Tkinter

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

O sensor DHT11 realiza a coleta dos valores de temperatura e umidade. O microcontrolador PIC16F877A processa essas informações e as transmite ao computador por meio da comunicação serial UART.

A aplicação desenvolvida em Python recebe os dados, realiza seu armazenamento em banco de dados SQLite e possibilita a visualização das medições por meio de gráficos.

## 📂 Estrutura do Projeto

```text
TCC-UNINTER-2026/
│
├── firmware/
│   └── PIC16F877A/
│       └── Teste.X/
│           ├── codigo.c
│           ├── Makefile
│           └── nbproject/
│
├── interface-grafica/
│
├── dados_sensor.db
├── database.py
├── interface_grafica.py
├── main.py
├── monitor_dht11.py
├── requirements.txt
├── serial_com.py
├── test.py
├── README.md
└── .gitignore
```

### Principais arquivos

- `firmware/PIC16F877A/Teste.X/` — projeto do firmware desenvolvido no MPLAB X para o PIC16F877A;
- `codigo.c` — código responsável pela leitura do sensor DHT11, processamento dos dados e comunicação do microcontrolador;
- `monitor_dht11.py` — realiza a recepção dos dados pela comunicação serial e o armazenamento das medições;
- `interface_grafica.py` — apresenta graficamente os valores de temperatura e umidade;
- `dados_sensor.db` — banco de dados SQLite utilizado para armazenar as medições;
- `requirements.txt` — dependências necessárias para execução da aplicação Python;
- `main.py`, `database.py`, `serial_com.py` e `test.py` — arquivos utilizados durante etapas de desenvolvimento e testes do sistema;
- `interface-grafica/` — implementação web experimental criada como possibilidade de expansão do projeto.

## 📡 Comunicação Serial

A comunicação entre o PIC16F877A e o computador utiliza UART com a seguinte configuração:

```text
Baud Rate: 9600
Clock: 20 MHz
TX: RC6
RX: RC7
Porta utilizada durante os testes: COM5
```

A porta serial pode variar de acordo com o computador utilizado.

## 🚀 Execução

Primeiramente, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Com o circuito conectado ao computador e a porta serial corretamente configurada, execute o programa responsável pela aquisição dos dados:

```bash
python monitor_dht11.py
```

Em outro terminal, execute a interface gráfica:

```bash
python interface_grafica.py
```

A aplicação realizará a leitura dos registros armazenados no banco de dados e apresentará os valores de temperatura e umidade graficamente.

## 📊 Resultados

Durante os testes realizados, o sistema apresentou funcionamento satisfatório, permitindo:

- Leitura da temperatura e da umidade;
- Comunicação entre o DHT11 e o PIC16F877A;
- Transmissão dos dados via UART;
- Recepção das informações utilizando Python;
- Armazenamento das medições em SQLite;
- Visualização gráfica dos dados;
- Criação de um histórico de medições.

O projeto demonstrou a viabilidade da utilização de uma solução embarcada de baixo custo para aplicações de monitoramento ambiental.

## 👨‍💻 Autor

**Carlos Eduardo Eiti Honma Antunes**  
Engenharia da Computação  
UNINTER — 2026

GitHub: [CarlosHonma](https://github.com/CarlosHonma)

## 🔗 Trabalho de Conclusão de Curso

Este repositório contém os códigos e arquivos desenvolvidos para o Trabalho de Conclusão de Curso:

**Sistemas Embarcados para Monitoramento de Temperatura e Umidade**

Repositório:  
https://github.com/CarlosHonma/TCC-UNINTER-2026
