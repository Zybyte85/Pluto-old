@echo off

pip "install" "-r" "requirements.txt"
pyinstaller "--onefile" "--windowed" "bin\main.py"