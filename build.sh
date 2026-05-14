#!/bin/bash

# 1. Construir la imagen
echo "Construyendo la imagen Docker..."
docker build -t pokemon-app .

# 2. Ejecutar el contenedor
echo "Ejecutando el contenedor..."
docker run -it --name pokeservice pokemon-app
