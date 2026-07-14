@echo off
REM AI Code Helper - Quick Start Script for Windows

echo 🚀 AI Code Helper - Quick Start
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
    echo ✅ Virtual environment created
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✨ AI Code Helper is ready!
echo.
echo 📝 To run the application:
echo    python app.py
echo.
echo 🌐 Then visit: http://localhost:8000
echo.
pause

python app.py
