#!/bin/bash
echo "Direcciones IP de esta Mac:"
ipconfig getifaddr en0 2>/dev/null || true
ipconfig getifaddr en1 2>/dev/null || true
echo "En otro dispositivo de la misma red, abra: http://IP_DE_ESTA_MAC:8501"
read -p "Presione Enter para cerrar..."
