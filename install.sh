#! /usr/bin/bash

# This packages the project into an executable

pip install -r requirements.txt

pyinstaller --onefile --windowed bin/main.py