#!/bin/bash

cd ~/VintedBot

while true
do
    echo "========================================"
    echo "🚀 Starting Vinted Hunter..."
    echo "$(date)"
    echo "========================================"

    source .venv/bin/activate

    python app.py

    echo ""
    echo "⚠️ Bot stopped."
    echo "Restarting in 5 seconds..."
    echo ""

    sleep 5
done