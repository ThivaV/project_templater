import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

if __name__ == "__main__":
    project_name = input('Enter the project name: ')
    project_path = input('Enter the project path: ')
    
    files = [
        '.github/workflows/.gitkeep',
        f'src/{project_name}/__init__.py',
        f'src/{project_name}/utils/__init__.py',
        f'src/{project_name}/config/__init__.py',
        f'src/{project_name}/config/configuration.py',
        f'src/{project_name}/pipeline/__init__.py',
        f'src/{project_name}/entity/__init__.py',
        f'src/{project_name}/constants/__init__.py',
        '.env ',
        'config/config.yaml',
        'dvc.yaml',
        'requirements.txt',
        'requirements_local.txt',
        'setup.py',
        f'notebooks/{project_name}.ipynb',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'models/__init__.py',
        'scripts/.gitkeep',
        'templates/index.html'
    ]
    
    for file in files:
        file_path = Path(file)
        file_path = os.path.join(project_path, file_path)
            
        file_dir, file_name = os.path.split(file_path)        
        
        if file_dir != '':
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f'creating directory: {file_dir} for the file: {file_name}')
        
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                logging.info(f'creating empty file: {file_path}')
                pass
        else:
            logging.info(f'{file_name} is already exists')
                