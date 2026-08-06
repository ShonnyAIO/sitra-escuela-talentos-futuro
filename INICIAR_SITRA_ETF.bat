@echo off
cd /d "%~dp0"
echo Iniciando SITRA-ETF v0.1...
echo Abra http://localhost:8501 si el navegador no abre automaticamente.
py -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
pause
