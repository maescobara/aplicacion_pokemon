import requests

pokemon_input = input("Nombre del Pokémon: ").lower()
url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_input}"

respuesta = requests.get(url_pokemon)

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    # 1. Extraer stats y tipo (tu código base)
    stats = {s["stat"]["name"]: s["base_stat"] for s in datos["stats"]}
    tipos = [t["type"]["name"] for t in datos["types"]]
    
    print(f"\n=== {datos['name'].upper()} ===")
    print(f"Tipo(s)  : {', '.join(tipos)}")
    print(f"HP       : {stats['hp']}    Ataque: {stats['attack']}")
    print(f"Velocidad: {stats['speed']}")

    # --- FUNCIÓN DE EVOLUCIONES ---
    print("\nLÍNEA EVOLUTIVA:")
    
    # Paso A: Obtener la URL de la especie (donde está el link a la cadena evolutiva)
    url_especie = datos["species"]["url"]
    datos_especie = requests.get(url_especie).json()
    
    # Paso B: Obtener la cadena de evolución completa
    url_evolucion = datos_especie["evolution_chain"]["url"]
    datos_evo = requests.get(url_evolucion).json()
    
    # Paso C: Recorrer la cadena (es un diccionario anidado)
    cadena = []
    actual = datos_evo["chain"]

    while actual:
        cadena.append(actual["species"]["name"].capitalize())
        # Si tiene evolución, pasamos al siguiente nodo (tomamos la primera opción)
        if actual["evolves_to"]:
            actual = actual["evolves_to"][0]
        else:
            actual = None

    print(" -> ".join(cadena))

else:
    print("Error: No se encontró ese Pokémon. Revisa la ortografía.")
 