import os
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
wkdirpth = os.getcwd()
print(os.listdir(wkdirpth))
logging.info('ML/DS Projects Structure Maker')

projectname = input('Enter project directory name with extension: ')
listdir = [
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/pipeline/__init__.py",
    "requirements.txt",
    "main.py",
    "research/trials.ipynb",
    "research/eda.ipynb",
    "templates/index.html"
]
listdir.append(projectname)
print(listdir)

print ("""
    1: src/{project_name}/utils/__init__.py, 
    2: src/{projectname}/config/__init__.py",
    3: src/{project_name}/config/configuration.py,
    4: src/{project_name}/entity/__init__.py,
    5: src/{project_name}/constants/__init__.py,
    6: Dockerfile file
    7: dvc.yaml,
    8: params.yaml,
    9: config/config.yaml,
    10: logger.py,
    11: exit """)

userchoose= input("")
def indirect(userchoose):
        switcher={
            1 : lambda: listdir.append("src/{projectname}/utils/__init__.py"),
            2 : lambda: listdir.append("src/{projectname}/config/__init__.py"),
            3 : lambda: listdir.append("src/{projectname}/config/configuration.py"),
            4 : lambda: listdir.append("src/{projectname}/entity/__init__.py"),
            5:  lambda: listdir.append("src/{projectname}/constants/__init__.py"),
            6:  lambda: listdir.append("Dockerfile"),
            7:  lambda: listdir.append("dvc.yaml"),
            8:  lambda: listdir.append("params.yaml"),
            9:  lambda: listdir.append('config/config.yaml'),
            10: lambda: listdir.append("logger.py"),
            11: lambda: exit()
            }
        func=switcher.get(userchoose,lambda :'Invalid')
        return func()
print(listdir)

x = input ("Want to insert Custom file, press y: ")
if x == 'y':
    user_input = input("Enter a file name with extension: ")
    listdir.append(user_input)
    print(listdir)
else: pass

for filepath in listdir:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")