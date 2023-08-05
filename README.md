# ML-DS-Projects-Structure-Maker
 ML/DS Projects Structure Maker is a python program that takes current path in directory (the path of the directory to be created) and `file_names` (a list of file names to be generated inside the directory).

<p>

On Linux use this command:
```
$ python template.py 
```
This produces the following result −
```
E:\mywork\projects\try>python template.py
['.github', 'proj']
2023-08-06 00:08:48,128: ML/DS Project directory maker
enter project directory name with extension: hello.py
['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py']

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
    11: exit
6
['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py']

Want to insert Custom  file, enter y: y
Enter a file name with extension: win.py

['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py', 'win.py']
2023-08-06 00:09:52,236: Creating directory; .github\workflows for the file: .gitkeep
2023-08-06 00:09:52,238: Creating empty file: .github\workflows\.gitkeep
2023-08-06 00:09:52,242: Creating directory; src\hello.py for the file: __init__.py
2023-08-06 00:09:52,244: Creating empty file: src\hello.py\__init__.py
2023-08-06 00:09:52,246: Creating directory; src\hello.py\components for the file: __init__.py
2023-08-06 00:09:52,280: Creating empty file: src\hello.py\components\__init__.py
2023-08-06 00:09:52,281: Creating directory; src\hello.py\pipeline for the file: __init__.py
2023-08-06 00:09:52,281: Creating empty file: src\hello.py\pipeline\__init__.py
2023-08-06 00:09:52,284: Creating empty file: requirements.txt
2023-08-06 00:09:52,287: Creating empty file: main.py
2023-08-06 00:09:52,289: Creating directory; research for the file: trials.ipynb
2023-08-06 00:09:52,292: Creating empty file: research\trials.ipynb
2023-08-06 00:09:52,294: Creating directory; research for the file: eda.ipynb
2023-08-06 00:09:52,297: Creating empty file: research\eda.ipynb
2023-08-06 00:09:52,300: Creating directory; templates for the file: index.html
2023-08-06 00:09:52,303: Creating empty file: templates\index.html
2023-08-06 00:09:52,306: Creating empty file: hello.py
2023-08-06 00:09:52,309: Creating empty file: win.py
```
On Windows
```
C:\Python34>Python template.py
```
This produces the following result −
```
E:\mywork\projects\try>python template.py
['.github', 'proj']
2023-08-06 00:08:48,128: ML/DS Project directory maker
enter project directory name with extension: hello.py
['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py']

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
    11: exit
6
['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py']

Want to insert Custom  file, enter y: y
Enter a file name with extension: win.py

['.github/workflows/.gitkeep', 'src/hello.py/__init__.py', 'src/hello.py/components/__init__.py', 'src/hello.py/pipeline/__init__.py', 'requirements.txt', 'main.py', 'research/trials.ipynb', 'research/eda.ipynb', 'templates/index.html', 'hello.py', 'win.py']
2023-08-06 00:09:52,236: Creating directory; .github\workflows for the file: .gitkeep
2023-08-06 00:09:52,238: Creating empty file: .github\workflows\.gitkeep
2023-08-06 00:09:52,242: Creating directory; src\hello.py for the file: __init__.py
2023-08-06 00:09:52,244: Creating empty file: src\hello.py\__init__.py
2023-08-06 00:09:52,246: Creating directory; src\hello.py\components for the file: __init__.py
2023-08-06 00:09:52,280: Creating empty file: src\hello.py\components\__init__.py
2023-08-06 00:09:52,281: Creating directory; src\hello.py\pipeline for the file: __init__.py
2023-08-06 00:09:52,281: Creating empty file: src\hello.py\pipeline\__init__.py
2023-08-06 00:09:52,284: Creating empty file: requirements.txt
2023-08-06 00:09:52,287: Creating empty file: main.py
2023-08-06 00:09:52,289: Creating directory; research for the file: trials.ipynb
2023-08-06 00:09:52,292: Creating empty file: research\trials.ipynb
2023-08-06 00:09:52,294: Creating directory; research for the file: eda.ipynb
2023-08-06 00:09:52,297: Creating empty file: research\eda.ipynb
2023-08-06 00:09:52,300: Creating directory; templates for the file: index.html
2023-08-06 00:09:52,303: Creating empty file: templates\index.html
2023-08-06 00:09:52,306: Creating empty file: hello.py
2023-08-06 00:09:52,309: Creating empty file: win.py
```
</p>
