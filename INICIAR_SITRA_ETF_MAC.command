#!/bin/bash
cd "$(dirname "$0")"
echo "Iniciando SITRA-ETF v0.1..."
echo "Abra http://localhost:8501 si el navegador no abre automaticamente."
python3 -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
read -p "Presione Enter para cerrar..."
