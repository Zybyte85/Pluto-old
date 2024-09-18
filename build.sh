#! /usr/bin/bash

# This packages the project into an executable

# Install the required Python packages
pip install -r requirements.txt

# Change to the project root directory
cd "$(dirname "$0")"

# Run PyInstaller with the specified options
pyinstaller --onefile --windowed --distpath . bin/main.py