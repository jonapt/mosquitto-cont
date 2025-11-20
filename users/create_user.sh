#!/bin/bash

# Obtener la ruta absoluta del directorio donde está el script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Ruta absoluta al password file
PASSWD_FILE="$SCRIPT_DIR/../mosquitto/config/passwords.txt"

# Crear carpetas si no existen
mkdir -p "$SCRIPT_DIR/../mosquitto/config"

# Crear archivo si no existe
if [ ! -f "$PASSWD_FILE" ]; then
    touch "$PASSWD_FILE"
fi

# Verificación de argumentos
if [ "$#" -lt 2 ]; then
    echo "Uso: $0 usuario contraseña"
    exit 1
fi

USER=$1
PASSWORD=$2

# Ejecutar mosquitto_passwd dentro de un contenedor temporal
docker run --rm \
    -v "$SCRIPT_DIR/../mosquitto/config:/mosquitto/config" \
    eclipse-mosquitto:2 \
    mosquitto_passwd -b /mosquitto/config/passwords.txt "$USER" "$PASSWORD"

echo "Usuario '$USER' creado/actualizado correctamente."

