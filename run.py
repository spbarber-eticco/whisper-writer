import os
import sys
import subprocess
from dotenv import load_dotenv
import argparse

print('Starting WhisperWriter...')
load_dotenv()
# subprocess.run([sys.executable, os.path.join('src', 'main.py')])

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Run WhisperWriter')
parser.add_argument('-c', '--config', action='store_true', help='Show configuration window on startup')
parser.add_argument('-r', '--run', action='store_true', help='Run directly without showing main window')
args = parser.parse_args()

# Preparar los argumentos para main.py
main_args = []
if args.config:
    main_args.append('--config')
if args.run:
    main_args.append('--run')

# Ejecutar main.py con los argumentos apropiados
subprocess.run([sys.executable, os.path.join('src', 'main.py')] + main_args)
