import tkinter as tk
import random
import time
import threading

# Função que simula leitura de sensor
def ler_sensor_simulado():
    temperatura = round(random.uniform(28.0, 40.0), 1)
    umidade = round(random.uniform(30.0, 80.0), 1)
    return temperatura, umidade

# Função que atualiza os dados na interface
def atualizar_dados():
    while True:
        temperatura, umidade = ler_sensor_simulado()

        temp_label.config(text=f"🌡 Temperatura: {temperatura:.1f} °C")
        umid_label.config(text=f"💧 Umidade: {umidade:.1f} %")

        if temperatura >= 35:
            alerta_label.config(
                text="⚠️ Alerta: Calor extremo! Beba água e evite esforço.", fg="red"
            )
        else:
            alerta_label.config(text="Temperatura dentro dos padrões.", fg="green")

        time.sleep(5)

# Iniciar monitoramento em thread
def iniciar_monitoramento():
    thread = threading.Thread(target=atualizar_dados)
    thread.daemon = True
    thread.start()

# Interface gráfica
app = tk.Tk()
app.title("Simulador de Clima")
app.geometry("400x250")
app.resizable(False, False)
app.configure(bg="#f0f0f0")

tk.Label(app, text="Simulador de Monitoramento de Calor", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

temp_label = tk.Label(app, text="🌡 Temperatura: -- °C", font=("Arial", 14), bg="#f0f0f0")
temp_label.pack(pady=5)

umid_label = tk.Label(app, text="💧 Umidade: -- %", font=("Arial", 14), bg="#f0f0f0")
umid_label.pack(pady=5)

alerta_label = tk.Label(app, text="", font=("Arial", 12), bg="#f0f0f0")
alerta_label.pack(pady=10)

iniciar_monitoramento()

app.mainloop()
