@echo off
setlocal

:: Check if Wi-Fi interfaces are present
netsh wlan show interfaces | findstr /i "State" > nul
if errorlevel 1 (
    echo No Wi-Fi interface detected. Running the Python script...
    python script.py
    exit /b
)

:: Get the Wi-Fi state (connected or disconnected)
for /f "tokens=2 delims=:" %%A in ('netsh wlan show interfaces ^| findstr /i "State"') do (
    set "wifiState=%%A"
)

:: Trim spaces from wifiState variable
set "wifiState=%wifiState: =%"

:: Evaluate Wi-Fi state
if /i "%wifiState%"=="connected" (
    echo Wi-Fi is connected. No action taken.
) else (
    echo Wi-Fi is not connected. Running the Python script...
    python script.py
)

endlocal
