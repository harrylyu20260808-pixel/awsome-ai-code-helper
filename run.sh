#!/bin/bash

# AI Code Helper - Quick Start Script

echo "🚀 AI Code Helper - Quick Start"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✨ AI Code Helper is ready!"
echo ""
echo "📝 To run the application:"
echo "   python app.py"
echo ""
echo "🌐 Then visit: http://localhost:8000"
echo ""
echo "Press Enter to start the server..."
read

python app.py
