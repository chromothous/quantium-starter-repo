#!/bin/bash

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Running tests..."
python -m pytest

if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi