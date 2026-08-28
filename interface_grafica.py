import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

 
# JANELA

janela = tk.Tk()
janela.title("Monitoramento DHT11")
janela.geometry("900x600")

# FRAME PRINCIPAL 

frame = ttk.Frame(janela)
frame.pack(fill="both", expand=True)

# FIGURA MATPLOTLIB 

figura = Figure(figsize=(8, 5), dpi=100)

grafico_temp = figura.add_subplot(211)
grafico_umid = figura.add_subplot(212)

canvas = FigureCanvasTkAgg(figura, master=frame)

canvas.get_tk_widget().pack(fill="both", expand=True)

# FUNÇÃO DE ATUALIZAÇÃO 

def atualizar_graficos():
    try:
        conexao = sqlite3.connect(
            "dados_sensor.db"
        )

        query = """
        SELECT * FROM leituras
        ORDER BY id DESC
        LIMIT 20
        """

        df = pd.read_sql_query(
            query,
            conexao
        )

        conexao.close()

        # coloca em ordem crescente
        df = df.iloc[::-1]

        # se não houver dados, limpa os gráficos e retorna
        if df.empty:
            grafico_temp.clear()
            grafico_umid.clear()
            grafico_temp.set_title("Temperatura")
            grafico_umid.set_title("Umidade")
            figura.tight_layout()
            canvas.draw()
            janela.after(5000, atualizar_graficos)
            return

        # parseia datas e extrai colunas
        try:
            horarios = pd.to_datetime(df["data_hora"])
        except Exception:
            horarios = df["data_hora"]

        temperaturas = df["temperatura"]

        umidades = df["umidade"]

        # LIMPA GRÁFICOS

        grafico_temp.clear()
        grafico_umid.clear()

        # TEMPERATURA

        grafico_temp.plot(
            horarios,
            temperaturas,
            marker='o'
        )

        grafico_temp.set_title(
            "Temperatura"
        )

        grafico_temp.set_ylabel(
            "°C"
        )

        grafico_temp.tick_params(
            axis='x',
            rotation=45
        )

        # UMIDADE

        grafico_umid.plot(
            horarios,
            umidades,
            marker='o'
        )

        grafico_umid.set_title(
            "Umidade"
        )

        grafico_umid.set_ylabel(
            "%"
        )

        grafico_umid.tick_params(
            axis='x',
            rotation=45
        )

        figura.tight_layout()

        canvas.draw()

    except Exception as erro:

        print("Erro gráfico:")
        print(erro)

    # atualiza a cada 5 segundos
    janela.after(5000, atualizar_graficos)

 
# INICIA ATUALIZAÇÃO
 

atualizar_graficos()

 
# LOOP DA INTERFACE
 

janela.mainloop()