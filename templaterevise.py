import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
wkdirpth = os.getcwd()
print(os.listdir(wkdirpth))
logging.info('ML/DS Projects Structure Maker')

projectname = input('Enter project directory name: ')

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

# Show available additional files to create
print("""
    1: src/{projectname}/utils/__init__.py
    2: src/{projectname}/config/__init__.py
    3: src/{projectname}/config/configuration.py
    4: src/{projectname}/entity/__init__.py
    5: src/{projectname}/constants/__init__.py
    6: Dockerfile
    7: dvc.yaml
    8: params.yaml
    9: config/config.yaml
    10: logger.py
    11: exit
""")

userchoose = int(input("Choose a number to add a file or 11 to exit: "))

def indirect(choice):
    switcher = {
        1: lambda: listdir.append(f"src/{projectname}/utils/__init__.py"),
        2: lambda: listdir.append(f"src/{projectname}/config/__init__.py"),
        3: lambda: listdir.append(f"src/{projectname}/config/configuration.py"),
        4: lambda: listdir.append(f"src/{projectname}/entity/__init__.py"),
        5: lambda: listdir.append(f"src/{projectname}/constants/__init__.py"),
        6: lambda: listdir.append("Dockerfile"),
        7: lambda: listdir.append("dvc.yaml"),
        8: lambda: listdir.append("params.yaml"),
        9: lambda: listdir.append('config/config.yaml'),
        10: lambda: listdir.append("logger.py"),
        11: exit
    }
    func = switcher.get(choice, lambda: logging.warning('Invalid choice'))
    return func()

# Call the indirect function to add the chosen file
indirect(userchoose)

x = input("Want to insert a custom file? Press y: ")
if x.lower() == 'y':
    user_input = input("Enter a file name with extension: ")
    listdir.append(user_input)

print("Final list of files to create:")
print(listdir)

# Boilerplate content for each file
boilerplate = {
    "__init__.py": "# This is an empty init file.",
    "main.py": "# Main entry point for the application.",
    "requirements.txt": "# List of dependencies.",
    "Dockerfile": "FROM python:3.8\n\n# Set the working directory\nWORKDIR /app\n\n# Copy the requirements file\nCOPY requirements.txt .\n\n# Install dependencies\nRUN pip install --no-cache-dir -r requirements.txt\n\n# Copy the rest of the application\nCOPY . .\n\n# Command to run the application\nCMD [ \"python\", \"main.py\" ]",
    "dvc.yaml": "# DVC pipeline configuration.",
    "params.yaml": "# Parameters for the project.",
    "config/config.yaml": "# Configuration settings.",
    "logger.py": "import logging\n\n# Configure logging\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')\n\nlogger = logging.getLogger(__name__)\n",
    "src/{projectname}/config/configuration.py": "# Configuration settings for the project.",
}

# Create directories and files with boilerplate code
for filepath in listdir:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            content = boilerplate.get(filename, "# Empty file.")
            f.write(content)
            logging.info(f"Creating file: {filepath} with boilerplate content.")
    else:
        logging.info(f"{filename} already exists")
