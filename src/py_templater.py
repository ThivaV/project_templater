import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

if __name__ == "__main__":
    project_name = input('Enter the project name: ')
    project_path = input('Enter the project path: ')

    proj_opt = '\nSelect the project structre:\n\t1=For master project structure\n\t2=For minimal project structre\n\t3=For cookbooks\n\t4=For general\n\t5=For kaggle competition\nEnter the number:'
    project_opt = input(proj_opt)
    
    # master project structure
    opt_1 = [
        '.github/workflows/.gitkeep',
        f'src/{project_name}/__init__.py',
        f'src/{project_name}/utils/__init__.py',
        f'src/{project_name}/config/__init__.py',
        f'src/{project_name}/components/__init__.py',
        f'src/{project_name}/config/configuration.py',
        f'src/{project_name}/pipeline/__init__.py',
        f'src/{project_name}/entity/__init__.py',
        f'src/{project_name}/constants/__init__.py',
        '.env',
        'config/config.yaml',
        'params.yaml'
        'dvc.yaml',
        'requirements.txt',
        'requirements_local.txt',
        'setup.py',
        'app.py',
        'main.py',
        f'notebooks/{project_name}.ipynb',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'docs/img/.gitkeep',
        'docs/doc/.gitkeep',
        'models/.gitkeep',
        'scripts/.gitkeep',
        'templates/index.html',
    ]

    # minimal project structre
    opt_2 = [
        '.github/workflows/.gitkeep',
        '.env',
        'requirements.txt',
        'requirements_local.txt',
        'setup.py',
        'app.py',
        'main.py',
        f'notebooks/{project_name}.ipynb',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'docs/img/.gitkeep',
        'docs/doc/.gitkeep',
        'models/.gitkeep',
        'scripts/.gitkeep',
        f'src/{project_name}/__init__.py',
    ]

    # cookbooks
    opt_3 = [
        '.github/workflows/.gitkeep',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'models/.gitkeep',
        f'notebooks/{project_name}.ipynb',
        'requirements_local.txt',
        'scripts/.gitkeep',
        '.env',
        'docs/img/.gitkeep',
        'docs/doc/.gitkeep'
    ]

    # general
    opt_4 = [
        '.github/workflows/.gitkeep',
        '.env',
        'requirements.txt',
        'requirements_local.txt',
        'app.py',
        'notebooks/.gitkeep',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'docs/img/.gitkeep',
        'docs/doc/.gitkeep',
        'models/.gitkeep',
        'scripts/.gitkeep',
        'src/__init__.py',
    ]

    # kaggle
    opt_5 = [
        '.github/workflows/.gitkeep',
        '.env',
        'requirements.txt',
        'requirements_local.txt',
        'app.py',
        'notebooks/.gitkeep',
        'data/master_data/.gitkeep',
        'data/processed_data/.gitkeep',
        'docs/img/.gitkeep',
        'docs/doc/.gitkeep',
        'models/.gitkeep',
        'scripts/.gitkeep',
        'src/__init__.py',
    ]

    if project_opt=='1':
        files=opt_1
    elif project_opt=='2':
        files=opt_2
    elif project_opt=='3':
        files=opt_3
    elif project_opt=='4':
        files=opt_4
    elif project_opt=='5':
        files=opt_5
    else:
        files=opt_2

    local_requirements_packages = ['ipykernel', 'ipywidgets', 'tqdm', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'python-dotenv', 'python-box']
    
    for file in files:
        file_path = Path(file)
        file_path = os.path.join(project_path, file_path)
            
        file_dir, file_name = os.path.split(file_path)        
        
        if file_dir != '':
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f'creating directory: {file_dir} for the file: {file_name}')
        
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                if file_name == 'requirements_local.txt':
                    # add kagglehub for kaggle works
                    if project_opt=='5':
                        local_requirements_packages.append('kagglehub')

                    for package in local_requirements_packages:
                        f.write(package + '\n')

                    logging.info(f'creating file with items: {file_path}')
                else:
                    logging.info(f'creating empty file: {file_path}')

                pass
        else:
            logging.info(f'{file_name} is already exists')
                