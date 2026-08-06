#!/bin/bash
cd "$(dirname "$0")"
echo "Instalando requisitos para SITRA-ETF v0.1..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
echo "Instalacion completada."
read -p "Presione Enter para cerrar..."
