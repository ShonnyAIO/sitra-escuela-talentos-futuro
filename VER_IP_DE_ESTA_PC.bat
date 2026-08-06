@echo off
echo Buscando direccion IPv4 de esta PC...
ipconfig | findstr /i "IPv4"
echo.
echo En otro dispositivo de la misma red, abra: http://IP_DE_ESTA_PC:8501
pause
