@echo off
echo.
echo ---------------------------------------------------------------------
echo   ISP Letter Generator - Builder
echo ---------------------------------------------------------------------
echo.

:: 1. Check for Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is NOT installed or not in your PATH.
    echo.
    echo To build this application, you must handle Python installed ONCE.
    echo After building, the resulting .exe file will run ANYWHERE without Python.
    echo.
    echo Please install Python from python.org and check "Add to PATH".
    pause
    exit /b
)

echo [INFO] Python found. Preventing conflicts...

:: 2. Install Requirements
echo [INFO] Installing Dependencies (this may take a minute)...
python -m pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install requirements. Check internet connection.
    pause
    exit /b
)

python -m pip install pyinstaller
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install PyInstaller.
    pause
    exit /b
)

:: 3. Build Executable
echo [INFO] Building Executable...
python -m PyInstaller --noconfirm ^
    --onefile ^
    --windowed ^
    --name "ISP_Letter_Gen" ^
    --add-data "app.py;." ^
    --add-data "backend.py;." ^
    --add-data "JIO Template.docx;." ^
    --add-data "Airtel Template.docx;." ^
    --add-data "VI Template.docx;." ^
    --add-data "JIO IP.xlsx;." ^
    --add-data "Airtel Format.xlsx;." ^
    --hidden-import "streamlit" ^
    --hidden-import "pandas" ^
    --hidden-import "openpyxl" ^
    --hidden-import "docx" ^
    --hidden-import "bs4" ^
    --hidden-import "ipwhois" ^
    --copy-metadata streamlit ^
    run_app.py

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build Failed! See error message above.
    pause
    exit /b
)

echo.
echo ---------------------------------------------------------------------
echo   SUCCESS! 
echo ---------------------------------------------------------------------
echo.
echo Your app is ready in the 'dist' folder.
echo You can now copy 'ISP_Letter_Gen.exe' to any computer.
echo.
pause
