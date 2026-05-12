import requests
import os

# Cumplimiento de no hardcoding
API_TOKEN = os.getenv("POKEAPI_KEY")

def consultar_pokemon():
    pokemon_input = input("Nombre del Pokémon: ").lower().strip()
    if not pokemon_input:
        return

    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_input}"

    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}
        respuesta = requests.get(url_pokemon, headers=headers, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        # --- 1. NOMBRE ---
        print(f"\n=== {datos['name'].upper()} ===")

        # --- 2. LINK CON LA IMAGEN ---
        print(f"Imagen: {datos['sprites']['front_default']}")

        # Consultamos especie para la descripción
        url_especie = datos["species"]["url"]
        res_especie = requests.get(url_especie, timeout=10)
        res_especie.raise_for_status()
        datos_especie = res_especie.json()

        # --- 3. DESCRIPCIÓN Y HABILIDADES ---
        descripciones = [ent["flavor_text"] for ent in datos_especie["flavor_text_entries"] if ent["language"]["name"] == "es"]
        if descripciones:
            texto = " ".join(descripciones[0].split())
            print(f"\nDescripción: {texto}")

        habilidades = [h["ability"]["name"].replace("-", " ").capitalize() for h in datos["abilities"]]
        print(f"Habilidades: {', '.join(habilidades)}")

        # --- LÓGICA DE TIPOS (Ventajas y Debilidades) ---
        tipos_nombres = [t["type"]["name"] for t in datos["types"]]
        ventajas = set()
        debilidades = set()

        for tipo in tipos_nombres:
            res_tipo = requests.get(f"https://pokeapi.co/api/v2/type/{tipo}", timeout=10)
            if res_tipo.status_code == 200:
                relaciones = res_tipo.json()["damage_relations"]
                # Tipos a los que les hace más daño (Ventaja)
                for v in relaciones["double_damage_to"]:
                    ventajas.add(v["name"].capitalize())
                # Tipos que le hacen más daño (Debilidad)
                for d in relaciones["double_damage_from"]:
                    debilidades.add(d["name"].capitalize())

        # --- 4. VENTAJAS ---
        print(f"\nEs fuerte contra: {', '.join(ventajas) if ventajas else 'Ninguno'}")

        # --- 5. DEBILIDADES ---
        print(f"Es débil contra  : {', '.join(debilidades) if debilidades else 'Ninguno'}")

        # --- 6. ESTADÍSTICAS ---
        stats = {s["stat"]["name"]: s["base_stat"] for s in datos["stats"]}
        print(f"\nESTADÍSTICAS:")
        print(f"Tipo(s)            : {', '.join([t.capitalize() for t in tipos_nombres])}")
        print(f"HP (Vida)          : {stats.get('hp')}")
        print(f"Ataque             : {stats.get('attack')}")
        print(f"Defensa            : {stats.get('defense')}")
        print(f"Ataque Especial    : {stats.get('special-attack')}")
        print(f"Defensa Especial   : {stats.get('special-defense')}")
        print(f"Velocidad          : {stats.get('speed')}")

        # --- 7. LÍNEA EVOLUTIVA ---
        print("\nLÍNEA EVOLUTIVA:")
        url_evolucion = datos_especie["evolution_chain"]["url"]
        datos_evo = requests.get(url_evolucion, timeout=10).json()
        
        cadena = []
        actual = datos_evo["chain"]
        while actual:
            cadena.append(actual["species"]["name"].capitalize())
            if actual["evolves_to"]:
                actual = actual["evolves_to"][0]
            else:
                break
        print(" -> ".join(cadena))

    except requests.exceptions.HTTPError:
        print(f"❌ Error: El Pokémon '{pokemon_input}' no existe.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de Red: Revisa tu conexión.")
    except requests.exceptions.Timeout:
        print("❌ Error de Tiempo: La API tardó demasiado.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    consultar_pokemon()
 