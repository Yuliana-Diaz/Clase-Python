import tkinter as tk
from tkinter import ttk 
from clase import Distancia

def convertirMetrosAKilometros():
    metros => 0.0
    try:
        metros = float(input_distancia.get())
        etiqueta_error_metros.config(text=f"")
    except ValueError as ve: 
        etiqueta_error_metros.config(text=f"Introduce un valor numérico")

    #crear un objeto de la clase Distancia
    conversionDistancia = Distancia()
    etiqueta_kilometros.config(text=f"Los kilómetros son: {conversionDistancia.convertirMetrosAKilometros(metros)}")
    etiqueta_centimetros.config(text=f"Los centímetros son: {conversionDistancia.convertirMetrosACentimetros(metros)}")
    etiqueta_milimetros.config(text=f"Los milímetros son: {conversionDistancia.convertirMetrosAMilimetros(metros)}")

ventana = tk.Tk()
ventana.title("Conversión de Distancia")
ventana.config(width=500, height=300)

# Etiqueta
etiqueta_metros = ttk.Label(text="Introduce la cantidad de metros:")
etiqueta_metros.place(x=10, y=10)

# Input o TextBox
input_distancia = ttk.Entry()
input_distancia.place(x=200, y=10, width=80)

# etiquetas para los errores
etiqueta_error_metros = ttk.Label(text="")
etiqueta_error_metros.place(x=300, y=10)

# Botón
boton_convertir = ttk.Button(text="Convertir", command=convertirMetrosAKilometros)
boton_convertir.place(x=90, y=40)

etiqueta_kilometros = ttk.Label(text="Los kilómetros son:")
etiqueta_kilometros.place(x=10, y=80)
etiqueta_centimetros = ttk.Label(text="Los centímetros son:")
etiqueta_centimetros.place(x=10, y=100)
etiqueta_milimetros = ttk.Label(text="Los milímetros son:")
etiqueta_milimetros.place(x=10, y=120)
ventana.mainloop()