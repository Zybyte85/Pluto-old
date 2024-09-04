#! /usr/bin/bash

# This packages the project into an executable

pip install pyinstaller

pyinstaller --onefile --windowed bin/main.py