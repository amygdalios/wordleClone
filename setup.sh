#!/bin/bash

# Check for python3 first
if command -v python3 &>/dev/null; then
    echo "🚀 Python3 is installed: $(python3 --version)"

    echo "⚙️ Setting up virtual enviroment"
    python3 -m venv venv

    echo "🔨 Installing requirements"
    pip install -r requirements.txt

    exit 0
elif command -v python &>/dev/null; then
    echo "🚀 Python is installed: $(python --version)"

    echo "⚙️ Setting up virtual enviroment"
    python -m venv venv

    echo "🔨 Installing requirements"
    pip install -r requirements.txt

    exit 0
else
    echo "Error: Python is not installed!" >&2
    exit 1
fi
