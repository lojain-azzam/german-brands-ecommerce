#!/bin/bash

echo "🇩🇪 German Brands PRD Showcase"
echo "================================"
echo "Starting 3D Interactive PRD Showcase..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 server.py
elif command -v python &> /dev/null; then
    python server.py
else
    echo "❌ Python not found. Please install Python 3 to run the server."
    exit 1
fi
