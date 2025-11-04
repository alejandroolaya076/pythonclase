import re
import os
import tkinter as tk
from tkinter import messagebox


def validar_correo():
    email = entrada.get().strip()

  
    arroba = re.search('@', email)
    punto = re.search(r'\.', email)

    if arroba and punto:
       
        nombre = email.split('@')[0]
        resultado = f" Correo válido: {email}\n Usuario: {nombre}\n"
        messagebox.showinfo("Resultado", resultado)

        ruta_archivo = os.path.join(os.getcwd(), "resultado_correo.txt")
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(resultado + "\n")

    else:
        resultado = " Correo inválido: falta '@' o '.'"
        messagebox.showerror("Error", resultado)


ventana = tk.Tk()
ventana.title("Validador de Correos")
ventana.geometry("400x220")


titulo = tk.Label(
    ventana, text="VALIDADOR DE CORREOS")
titulo.pack(pady=10)
etiqueta = tk.Label(
    ventana, text="Ingresa un correo electrónico:", )
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack(pady=10)
boton = tk.Button(
    ventana, text="Validar",  
    command=validar_correo
)
boton.pack(pady=10)
ventana.mainloop()

