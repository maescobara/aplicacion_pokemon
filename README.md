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

## Automatización con Jenkins (CI/CD)

El proyecto cuenta con un flujo de integración y despliegue continuo configurado en Jenkins utilizando dos trabajos principales que interactúan de forma segura.

### 1. BuildAppJob (Trabajo de Estilo Libre)
* **Función:** Clona de forma automatizada este repositorio utilizando credenciales seguras de GitHub (impidiendo la exposición de tokens en texto plano) y ejecuta el script de automatización `build.sh`.
* **Resultado:** Construye la imagen Docker, levanta el contenedor e imprime en su salida de consola (`Console Output`) los datos reales obtenidos directamente desde la PokeAPI.

### 2. SamplePipeline (Trabajo de Tipo Pipeline)
Orquesta el ciclo de vida de la aplicación mediante un script inline estructurado en dos etapas secuenciales independientes para garantizar la visibilidad en el Stage View:
* **Etapa 1: Preparation:** Se encarga de detener y eliminar cualquier contenedor previo existente (`pokeservice`) utilizando `catchError` para asegurar que el pipeline continúe con éxito (en verde) incluso si no hay contenedores activos en la primera ejecución.
* **Etapa 2: Build:** Invoca secuencialmente a `BuildAppJob` para ejecutar la clonación, compilación y despliegue final del contenedor.

---

## Evidencias de la Evaluación

Todos los archivos gráficos e informativos que respaldan el correcto funcionamiento de la automatización se encuentran almacenados de forma estricta en la carpeta `/evidencias/jenkins/` de este repositorio:

1. `credentials.png`: Muestra el token de GitHub configurado de forma segura dentro del gestor de credenciales globales de Jenkins (oculto en texto plano).
2. `stage_view.png`: Captura del Stage View de `SamplePipeline` reflejando las dos etapas (`Preparation` y `Build`) completadas exitosamente en verde brillante con sus respectivos tiempos de ejecución.
3. `console_output_build.png`: Registro de la salida de consola de `BuildAppJob` que demuestra la construcción de la imagen, inicialización del contenedor y la respuesta con datos reales extraídos de la API.
4. `pipeline_script.txt`: Archivo con el código Groovy exacto utilizado de forma inline para orquestar las etapas del pipeline.