@echo off
cd /d "%~dp0"
echo Instalando requisitos para SITRA-ETF v0.1...
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
echo.
echo Instalacion completada.
pause
