Poké-data Competitivo (VGC Tool)

- Stakeholder: ¿Quién usa la herramienta?

Mi aplicación esta destinada a los fanáticos, jugadores/Entrenadores competitivos de la franquicia "Pokémon" ya que les otorgara datos técnicos precisos (estadísticas base, ventajas/debilidades de tipo y regiones de origen) para optimizar la formación de equipos de batalla en torneos casuales o competitivos (VGC).


- Propuesta de Valor (Problema/Solución): ¿Qué dificultad elimina?

Mi aplicación despejara las dudas sin la necesidad de investigar y navegar por distintos foros/wikis de "Pokémon" agrupando en una sola consulta de consola, información que generalmente requiere tres o cuatro búsquedas distintas sobre el mismo pokémon, tales como descripción del espécimen, estadísticas exactas para cálculo de daño, relaciones de ventaja/debilidad de tipo y su línea evolutiva, permitiendo tomar decisiones de forma mas rapida.


- Guía de Configuración
La API no requiere autenticación, pero se implementa soporte para headers como práctica de seguridad y para cumplir evitar el "hardcoding" de credenciales, mi aplicación utiliza variables de entorno para la gestión de tokens de API.

Variable de Entorno: `POKEAPI_KEY`
* * Descripción: Si bien la API de PokeAPI es de libre uso y no requiere autenticación, el script está diseñado para soportar el envío de tokens mediante variables de entorno utilizando la librería `os` de Python, como práctica de desarrollo segura y escalable.

---

- Instrucciones de Ejecución (Docker)
Para asegurar la portabilidad del software, el script ha sido contenerizado utilizando Docker.

*Requisitos previos*
* Tener Docker instalado y en ejecución.
* Contar con acceso a internet para el consumo de la API.

- Construcción de la Imagen
Desde la raíz del proyecto, ejecute:
```bash
docker build -t pokemon-app .