import os, sys
from pathlib import Path

workspace_loc = r'H:\projects\bgremover'

dir_list = [    'src', 
            'templates',
            'logs']

file_list = ['src/bgrem/pipeline/__init__.py', 
            'src/bgrem/config/__init__.py', 
            'src/bgrem/utils/__init__.py', 
            'src/bgrem/components/__init__.py', 
            'src/bgrem/__init__.py', 
            'config/config.yaml']

for folder in dir_list:
    os.makedirs(folder, exist_ok=True)

for file in file_list:
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'w') as f:
        pass
    