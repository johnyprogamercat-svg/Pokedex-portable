import io
import requests
import tkinter as tk
from PIL import Image, ImageTk
print("Bienvenido al pokedex portable")
def consultar_pokemon():
    pokemon = caja_busqueda.get().lower().replace(" ", "-")
    url_pok = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    respuesta = requests.get(url_pok)
    if respuesta.status_code == 200:
        print("Pokemon encontrado!")
        datos = respuesta.json()
        info = ""
        info += f"ID: {datos['id']}\n"
        info += f"Nombre: {datos['name']}\n"
        info += f"Altura: {datos['height']}\n"
        info += f"Peso: {datos['weight']}\n"
        info += f"Experiencia base: {datos['base_experience']}\n"

        for tipo in datos["types"]:
            info += f"Tipo: {tipo['type']['name']}\n"
        url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"
        respuesta_especie = requests.get(url_especie)
        if respuesta_especie.status_code == 200:
            datos_especie = respuesta_especie.json()
            info += f"Generación: {datos_especie['generation']['name']}\n"
        etiqueta_resultado.config(text=info)

        primer_tipo = datos["types"][0]["type"]["name"]
        
        if primer_tipo == "fire":
            ventana.config(bg = "#e25919")
        elif primer_tipo == "water":
            ventana.config(bg = "#134198")
        elif primer_tipo == "grass" or primer_tipo == "bug":
            ventana.config(bg = "#139867")
        elif primer_tipo == "dark" or primer_tipo == "ghost" or primer_tipo == "poison":
            ventana.config(bg = "#15072F")
        elif primer_tipo == "ice":
            ventana.config(bg = "#2FD0F8")
        elif primer_tipo == "rock" or primer_tipo == "ground" or primer_tipo == "fighting":
            ventana.config(bg = "#542D16")
        elif primer_tipo == "electric":
            ventana.config(bg = "#F7F314")
        elif primer_tipo == "steel" or primer_tipo == "flying":
            ventana.config(bg = "#A0A8B6")
        elif primer_tipo == "dragon":
            ventana.config(bg = "#07073A")
        elif primer_tipo == "fairy" or primer_tipo == "psychic":
            ventana.config(bg = "#E66BE4")
        else:
            ventana.config(bg = "#FBF8F8")
        url_imagen = datos["sprites"]["front_default"]
        if url_imagen:
            respuesta_img = requests.get(url_imagen)
            imagen_bytes = io.BytesIO(respuesta_img.content)
            imagen_pil = Image.open(imagen_bytes)
            imagen_pil = imagen_pil.resize((240, 240), Image.Resampling.NEAREST)
            global imagen_tk
            imagen_tk = ImageTk.PhotoImage(imagen_pil)
            etiqueta_imagen.config(image=imagen_tk)
        else:
            etiqueta_imagen.config(image="")
    else:
        etiqueta_resultado.config(text="Este Pokemón no existe")

ventana = tk.Tk()
ventana.title("Pokedex portable")
ventana.geometry("380x450")
titulo = tk.Label(ventana, text="POKÉDEX PORTABLE", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

etiqueta_instruccion = tk.Label(ventana, text="Nombre del Pokémon:", font=("Arial", 10))
etiqueta_instruccion.pack(pady=5)

caja_busqueda = tk.Entry(ventana, font=("Arial", 12), justify="center")
caja_busqueda.pack(pady=5)

# Aquí conectamos el botón con la función usando 'command'
boton_buscar = tk.Button(ventana, text="Buscar", font=("Arial", 10, "bold"), bg="#3e19e2", fg="white", command=consultar_pokemon)
boton_buscar.pack(pady=10)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="Escribe un Pokémon y presiona Buscar.", font=("Arial", 10), justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
