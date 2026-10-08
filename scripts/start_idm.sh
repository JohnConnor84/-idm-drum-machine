#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

if ! command -v pd >/dev/null 2>&1; then
    echo "ERROR: Pure Data (pd) no está instalado."
    exit 1
fi

echo "IDM Drum Machine v0.1"
echo "Scanning sample banks..."

python3 scripts/scan_banks.py

echo "Starting Pure Data..."
exec pd -nogui -rt -r 48000 -open "$PROJECT_DIR/pd/idm_drum_machine.pd"
