# 🌡️ Sistema Embarcado para Monitoramento de Temperatura e Umidade

Sistema embarcado desenvolvido para realizar o **monitoramento de temperatura e umidade em tempo real**, utilizando o microcontrolador **PIC16F877A** e o sensor **DHT11**.

Os dados coletados pelo microcontrolador são enviados ao computador por meio de **comunicação serial UART**, onde uma aplicação desenvolvida em **Python** realiza a leitura, armazenamento e visualização das informações.

O projeto integra conceitos de **sistemas embarcados, programação de microcontroladores, comunicação serial, banco de dados e visualização de dados**.

---

## 📌 Objetivo

Desenvolver uma solução de baixo custo capaz de:

* Monitorar temperatura e umidade do ambiente;
* Realizar a leitura do sensor DHT11 utilizando o PIC16F877A;
* Transmitir os dados para um computador via UART;
* Receber e processar os dados utilizando Python;
* Armazenar as medições em um banco de dados SQLite;
* Exibir as informações coletadas por meio de gráficos;
* Manter um histórico das medições realizadas.

---

## 🏗️ Arquitetura do Sistema

O funcionamento geral do projeto pode ser representado pelo seguinte fluxo:

```text
┌─────────────┐
│    DHT11    │
│ Temperatura │
│  e Umidade  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ PIC16F877A  │
│  Firmware C │
└──────┬──────┘
       │
       │ UART
       ▼
┌─────────────┐
│ USB / Serial│
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Aplicação Python │
└──────┬───────────┘
       │
       ├──────────────► SQLite
       │
       └──────────────► Pandas / Matplotlib
```

---

## 🔧 Hardware Utilizado

* **Microcontrolador:** PIC16F877A
* **Sensor:** DHT11
* **Placa:** PIC DIP40
* **Cristal:** 20 MHz
* **Programador:** PICkit 3
* **Comunicação:** UART
* **Interface com o computador:** USB/Serial

O **DHT11** é responsável pela aquisição das informações de temperatura e umidade, enquanto o **PIC16F877A** realiza o processamento e transmissão dos dados.

---

## 💻 Tecnologias Utilizadas

### Firmware

* Linguagem C
* MPLAB X IDE
* Compilador XC8
* PIC16F877A

### Aplicação

* Python
* PySerial
* Pandas
* Matplotlib
* SQLite

---

## 🔄 Funcionamento

O sistema funciona seguindo as seguintes etapas:

1. O sensor **DHT11** realiza a medição da temperatura e da umidade relativa do ambiente.
2. O **PIC16F877A** solicita e recebe os dados do sensor.
3. O firmware processa e valida as informações recebidas.
4. Os valores são enviados ao computador utilizando **UART**.
5. A aplicação em **Python** recebe os dados através da porta serial.
6. As medições são armazenadas em um banco de dados **SQLite**.
7. Os dados são processados utilizando **Pandas**.
8. Os resultados são apresentados graficamente utilizando **Matplotlib**.

---

## 📡 Comunicação Serial

A comunicação entre o microcontrolador e o computador utiliza UART com a seguinte configuração:

```text
Baud Rate: 9600
Clock: 20 MHz
Modo: Assíncrono
TX: RC6
RX: RC7
```

O sistema envia os dados em formato legível, permitindo também acompanhar as medições utilizando um terminal serial.

Exemplo:

```text
Temperatura: 24°C
Umidade: 66%
```

---

## 🗄️ Armazenamento dos Dados

As informações recebidas pela aplicação são armazenadas utilizando **SQLite**.

O banco permite manter um histórico das medições realizadas pelo sistema, possibilitando posteriormente:

* Consultas de medições anteriores;
* Comparações entre períodos;
* Análise da variação da temperatura;
* Análise da variação da umidade;
* Identificação de tendências;
* Geração de gráficos.

---

## 📊 Visualização dos Dados

A aplicação Python utiliza:

**Pandas**

Responsável pela organização e manipulação dos dados coletados.

**Matplotlib**

Responsável pela geração dos gráficos utilizados para acompanhar as variações de temperatura e umidade.

A combinação dessas ferramentas permite visualizar o comportamento das variáveis ambientais ao longo do tempo.

---

## 📂 Estrutura do Projeto

A organização do repositório pode seguir a seguinte estrutura:

```text
.
├── firmware/
│   └── codigo_pic/
│
├── python/
│   ├── main.py
│   └── dados_sensor.db
│
├── docs/
│   ├── imagens/
│   └── relatorio/
│
├── README.md
└── .gitignore
```

> A estrutura pode ser adaptada de acordo com a organização atual dos arquivos do projeto.

---

## 🚀 Como Executar

### 1. Firmware

Abra o projeto utilizando o **MPLAB X IDE**.

Compile utilizando o compilador **XC8** e grave o firmware no PIC16F877A utilizando o **PICkit 3**.

---

### 2. Conecte o hardware

Certifique-se de que:

* O DHT11 está conectado corretamente;
* O PIC16F877A está alimentado;
* A comunicação serial está conectada ao computador;
* A porta serial foi reconhecida pelo sistema operacional.

---

### 3. Instale as dependências Python

```bash
pip install pyserial pandas matplotlib
```

---

### 4. Configure a porta serial

No código Python, configure a porta correspondente ao dispositivo.

Exemplo no Windows:

```python
porta = "COM5"
baudrate = 9600
```

A porta pode variar dependendo do computador utilizado.

---

### 5. Execute a aplicação

```bash
python main.py
```

A aplicação começará a receber as informações transmitidas pelo microcontrolador.

---

## 📈 Resultados

Durante os testes, o sistema conseguiu realizar com sucesso:

* Leitura de temperatura;
* Leitura de umidade;
* Comunicação entre DHT11 e PIC16F877A;
* Comunicação UART entre microcontrolador e computador;
* Recepção dos dados utilizando Python;
* Armazenamento das medições em SQLite;
* Geração de gráficos;
* Monitoramento das variáveis ambientais em tempo real.

Durante o desenvolvimento foram observadas algumas ocorrências de erro de **checksum** provenientes da comunicação com o DHT11. Ajustes de temporização foram realizados no firmware para melhorar a estabilidade da leitura.

Os testes demonstraram a viabilidade da utilização de uma solução embarcada de baixo custo para aplicações de monitoramento ambiental.

---

## 🔮 Possíveis Melhorias

O projeto pode ser expandido futuramente com funcionalidades como:

* Sistema de alertas para temperaturas críticas;
* Alertas de umidade;
* Dashboard web;
* Exportação dos dados para CSV;
* Geração automática de relatórios;
* Monitoramento remoto;
* Integração com Wi-Fi;
* Utilização de sensores de maior precisão;
* API para consulta das medições;
* Armazenamento dos dados em servidor ou nuvem.

---

## 🎓 Contexto Acadêmico

Projeto desenvolvido como **Trabalho de Conclusão de Curso (TCC)**, explorando a integração entre hardware e software para construção de um sistema embarcado de monitoramento ambiental.

O desenvolvimento permitiu aplicar conceitos relacionados a:

* Sistemas embarcados;
* Sistemas microprocessados;
* Microcontroladores;
* Sensores digitais;
* Comunicação UART;
* Programação em C;
* Programação em Python;
* Banco de dados;
* Aquisição de dados;
* Visualização de dados.

---

## 👨‍💻 Autor

**Carlos Eduardo Eiti Honma Antunes**

Engenharia da Computação

---

## 📚 Referências

* PÉRES, André Brandão. *Monitorador de temperatura e umidade do ar*. 2008.
* WOLF, Wayne. *Computers as Components: Principles of Embedded Computing System Design*. 2012.
* VALVANO, Jonathan W. *Embedded Systems*. 2017.
* FRADEN, Jacob. *Handbook of Modern Sensors*. 2016.
* Microchip Technology — documentação do PIC16F877A.
