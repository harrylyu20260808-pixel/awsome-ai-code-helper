#!/bin/bash

# AI Code Helper - Start Server Script

echo "🚀 Starting AI Code Helper Server..."
echo ""

cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run the server
python app.py
