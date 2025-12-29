# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import scrolledtext, Toplevel, filedialog
import subprocess

# Rutas iniciales
# Ruta al ejecutable llama-run (ajustar según tu sistema)
llama_executable = "/ruta/a/llama.cpp/build/bin/llama-run"

# Ruta al modelo GGUF (ajustar según tu sistema)
model_path = "/ruta/a/tu_modelo.gguf"


# Historial real
historial = []

# Función para enviar el mensaje y obtener la respuesta
def enviar_mensaje():
    mensaje = entrada.get().strip()
    if mensaje:
        # Agregar al historial
        historial.append(f"Tú: {mensaje}")

        # Mostrar mensaje en el chat
        chat.insert(tk.END, f"Tú: {mensaje}\n")
        chat.yview(tk.END)
        entrada.delete(0, tk.END)

        # Obtener respuesta
        ventana.after(100, lambda: obtener_respuesta(mensaje))

# Función para interactuar con el modelo
def obtener_respuesta(mensaje):
    command = [
        llama_executable,
        model_path,
        f"Responde en español: {mensaje}"
    ]
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        if result.returncode == 0:
            respuesta = result.stdout.strip() or "Error: No se recibió respuesta."
        else:
            respuesta = f"Error: {result.stderr.strip()}"
    except Exception as e:
        respuesta = f"Error al obtener respuesta: {str(e)}"

    # Agregar al historial
    historial.append(f"Asistente: {respuesta}")

    # Mostrar respuesta en el chat
    chat.insert(tk.END, f"Asistente: {respuesta}\n")
    chat.yview(tk.END)

# Función para cambiar fuente (volvemos al tamaño inicial)
def cambiar_fuente():
    chat.config(font=("Arial", 12))
    entrada.config(font=("Arial", 12))

# Función para alternar entre tema claro y oscuro
def alternar_tema():
    tema_actual = chat.cget("bg")
    if tema_actual == "white":
        # Cambiar a tema oscuro
        chat.config(bg="black", fg="white")
        entrada.config(bg="gray", fg="white")
    else:
        # Cambiar a tema claro
        chat.config(bg="white", fg="black")
        entrada.config(bg="white", fg="black")

# Función para mostrar historial
def mostrar_historial():
    ventana_historial = Toplevel(ventana)
    ventana_historial.title("Historial de Mensajes")
    ventana_historial.geometry("600x400")

    historial_texto = scrolledtext.ScrolledText(ventana_historial, wrap=tk.WORD, bg="white", fg="black", font=("Arial", 12))
    historial_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    historial_texto.insert(tk.END, "Historial de mensajes:\n")
    for mensaje in historial:
        historial_texto.insert(tk.END, f"{mensaje}\n")
    historial_texto.yview(tk.END)

# Función para cargar un modelo diferente
def cargar_modelo():
    global model_path
    archivo = filedialog.askopenfilename(title="Selecciona el archivo del modelo", filetypes=[("Modelos GGUF", "*.gguf")])
    if archivo:
        model_path = archivo
        chat.insert(tk.END, f"Modelo cargado: {model_path}\n")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Chat con LLaMA")
ventana.geometry("800x600")
ventana.config(bg="lightblue")

# Menú superior
def crear_menu():
    menu_bar = tk.Menu(ventana)

    # Menú de configuración
    menu_configuracion = tk.Menu(menu_bar, tearoff=0)
    menu_configuracion.add_command(label="Cambiar Fuente", command=cambiar_fuente)
    menu_configuracion.add_command(label="Alternar Tema", command=alternar_tema)
    menu_configuracion.add_command(label="Ver Historial", command=mostrar_historial)
    menu_configuracion.add_command(label="Cargar Modelo", command=cargar_modelo)
    menu_bar.add_cascade(label="Configuración", menu=menu_configuracion)

    ventana.config(menu=menu_bar)

crear_menu()

# Panel lateral
panel_lateral = tk.Frame(ventana, width=150, bg="lightgray", relief="sunken")
panel_lateral.grid(row=0, column=0, rowspan=2, sticky="ns", padx=5, pady=5)

btn_fuente = tk.Button(panel_lateral, text="Cambiar Fuente", command=cambiar_fuente)
btn_fuente.pack(padx=10, pady=5)

btn_tema = tk.Button(panel_lateral, text="Alternar Tema", command=alternar_tema)
btn_tema.pack(padx=10, pady=5)

btn_historial = tk.Button(panel_lateral, text="Ver Historial", command=mostrar_historial)
btn_historial.pack(padx=10, pady=5)

btn_cargar = tk.Button(panel_lateral, text="Cargar Modelo", command=cargar_modelo)
btn_cargar.pack(padx=10, pady=5)

# Área principal (chat + entrada)
frame_principal = tk.Frame(ventana)
frame_principal.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

chat = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD, bg="white", fg="black", font=("Arial", 12))
chat.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_entrada = tk.Frame(ventana)
frame_entrada.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

entrada = tk.Entry(frame_entrada, font=("Arial", 12))
entrada.pack(fill=tk.X, padx=10, pady=10, side=tk.LEFT)

boton_enviar = tk.Button(frame_entrada, text="Enviar", command=enviar_mensaje, bg="green", fg="yellow", relief="raised", font=("Arial", 12))
boton_enviar.pack(pady=10, side=tk.RIGHT)

# Vincular tecla "Enter" al envío del mensaje
ventana.bind("<Return>", lambda event: enviar_mensaje())

# Configurar redimensionamiento
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Iniciar bucle principal
ventana.mainloop()
