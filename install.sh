#!/bin/bash
set -e

echo "=== IDM Drum Machine v0.1 ==="

if [ "$(id -u)" -eq 0 ]; then
    echo "Ejecuta este instalador como usuario normal, sin sudo."
    exit 1
fi

if ! command -v apt-get >/dev/null 2>&1; then
    echo "Este instalador está diseñado para Raspberry Pi OS / Debian."
    exit 1
fi

sudo apt-get update
sudo apt-get install -y puredata python3

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

chmod +x "$PROJECT_DIR/scripts/start_idm.sh"
python3 -m py_compile "$PROJECT_DIR/scripts/scan_banks.py"

echo
echo "Instalación básica completada."
echo "Proyecto: $PROJECT_DIR"
echo
echo "Para probar el lanzador gráfico en la Raspberry Pi:"
echo "  $PROJECT_DIR/scripts/start_idm.sh"
echo
echo "Nota: el patch actual es un prototipo visual."
echo "La reproducción de samples, MIDI Clock y la interfaz completa"
echo "todavía requieren implementación y pruebas."

