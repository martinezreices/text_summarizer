import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

project_name = 'text_summarizer'


files = [
    '.github/workflows/.gitkeep/',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging//__init__.py',
    f'src/{project_name}/config__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/congig.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirememnts.txt',
    'setup.py'
    'research/trials.ipynb'
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)   # Separate the file name from file

    if filedir!= '':  # if file is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory:{filedir} for the ffile {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists')