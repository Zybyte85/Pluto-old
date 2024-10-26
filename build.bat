@echo off

pip "install" "-r" "requirements.txt"
cd "%undefined%"
pyinstaller "--onefile" "--windowed" "--distpath" "." "bin\main.py"