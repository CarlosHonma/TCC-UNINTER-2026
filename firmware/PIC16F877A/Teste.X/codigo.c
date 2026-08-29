#include <xc.h>

// CONFIGURAÇÃO
#define _XTAL_FREQ 4000000

#pragma config FOSC = XT
#pragma config WDTE = OFF
#pragma config PWRTE = ON
#pragma config BOREN = ON
#pragma config LVP = OFF
#pragma config CPD = OFF
#pragma config WRT = OFF
#pragma config CP = OFF

// VARIÁVEIS

unsigned char RH_byte1, RH_byte2;
unsigned char T_byte1, T_byte2;
unsigned char checksum;

// UART

void UART_Init() {
    TRISCbits.TRISC6 = 0;
    TRISCbits.TRISC7 = 1;
    TXSTAbits.SYNC = 0;
    TXSTAbits.BRGH = 1;
    SPBRG = 25;
    RCSTAbits.SPEN = 1;
    TXSTAbits.TXEN = 1;
    RCSTAbits.CREN = 1;
}

void UART_Write(char data) {
    while(PIR1bits.TXIF == 0);
    TXREG = data;
}

void UART_Write_Text(const char *text) {
    while(*text) {
        UART_Write(*text++);
    }
}

// DHT11

void Request() {
    TRISBbits.TRISB1 = 0;
    PORTBbits.RB1 = 0;
    __delay_ms(20);
    PORTBbits.RB1 = 1;
    __delay_us(30);
    TRISBbits.TRISB1 = 1;
}

unsigned char Response() {
    unsigned int timeout = 0;

    while(PORTBbits.RB1 == 1) {
        timeout++;

        __delay_us(1);

        if(timeout > 100)
            return 0;
    }

    timeout = 0;

    while(PORTBbits.RB1 == 0) {
        timeout++;

        __delay_us(1);

        if(timeout > 100)
            return 0;
    }

    timeout = 0;

    // espera low novamente
    while(PORTBbits.RB1 == 1) {
        timeout++;

        __delay_us(1);

        if(timeout > 100)
            return 0;
    }

    return 1;
}

// LEITURA DOS DADOS

unsigned char Receive_data() {
    unsigned char i;
    unsigned char data = 0;
    unsigned int count;

    for(i = 0; i < 8; i++) {
        count = 0;
        while(PORTBbits.RB1 == 0);
        while(PORTBbits.RB1 == 1) {
            count++;
            if(count > 1000)
                break;
        }

        data <<= 1;

        if(count > 3) {
            data |= 1;
        }
    }

    return data;
}

// MAIN

void main(void) {
    GIE = 0;
    PEIE = 0;

    ADCON1 = 0x06;
    TRISBbits.TRISB1 = 1;

    UART_Init();

    __delay_ms(2000);
    UART_Write_Text("Sistema iniciado\r\n\r\n");
    while(1) {
        Request();

        // verifica resposta do sensor
        if(Response()) {
            // leitura dos 5 bytes
            RH_byte1 = Receive_data();
            RH_byte2 = Receive_data();

            T_byte1 = Receive_data();
            T_byte2 = Receive_data();

            checksum = Receive_data();

            // verifica integridade
            if((RH_byte1 + RH_byte2 + T_byte1 + T_byte2) == checksum) {
                // temperatura
                UART_Write_Text("T:");

                UART_Write((T_byte1 / 10) + '0');
                UART_Write((T_byte1 % 10) + '0');

                UART_Write_Text("C\r\n");

                // umidade
                UART_Write_Text("U:");

                UART_Write((RH_byte1 / 10) + '0');
                UART_Write((RH_byte1 % 10) + '0');

                UART_Write_Text("%\r\n\r\n");
            }
            else {
                UART_Write_Text("Erro checksum\r\n\r\n");
            }
        }
        else {
            UART_Write_Text("Sensor nao responde\r\n\r\n");
        }

        // intervalo entre as leituras
        __delay_ms(10000);
    }
}