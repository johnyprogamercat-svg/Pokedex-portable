import tkinter as tk
ventana = tk.Tk()
ventana.title("Pokedex portable v1.0 by Dansmer")
ventana.geometry("400x500")

titulo = tk.Label(ventana, text="Pokedex portable", font=("Arial", 16, "bold"))
titulo.pack(pady=10)
etiqueta_instruccion = tk.Label(ventana, text="Nombre del Pokemón:", font=("Arial", 10))
etiqueta_instruccion.pack(pady=5)

caja_busqueda = tk.Entry(ventana, font=("Arial", 12), justify="center")
caja_busqueda.pack(pady=5)

boton_buscar = tk.Button(ventana, text="Buscar", font=("Arial", 10, "bold"), bg="#ff4d4d", fg="white")
boton_buscar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Escribe un Pokemón y presiona buscar", font=("Arial", 10), justify="left")
etiqueta_instruccion.pack(pady=20)

ventana.mainloop()