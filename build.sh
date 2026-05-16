#!/bin/bash

# 1. GENERAR EL DOCKERFILE
echo "Generando Dockerfile..."
cat <<EOF > Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "-u", "app.py"]
EOF

# 2. CONSTRUIR LA IMAGEN
echo "Construyendo la imagen Docker..."
docker build -t pokemon-app .

# 3. EJECUTAR EL CONTENEDOR
# Primero borramos si existe uno viejo para que no de error
docker rm -f pokeservice 2>/dev/null

echo "Ejecutando el contenedor..."
docker run -it --name pokeservice pokemon-app
