#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3 and try again."
    exit 1
fi

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found. Creating one with default content."
    echo "argparse==1.4.0" > requirements.txt
fi

# Install dependencies
pip install -r requirements.txt

echo "Environment setup complete. To activate the environment, run:"
echo "source env/bin/activate"