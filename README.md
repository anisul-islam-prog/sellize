# sellize

A Ecommerce Website using django framework

## How to Install

After Cloning the repo:

### Create a Virtual Environment:

> Unix Based OS :

`virtualenv venv`

> Windows :

`python -m venv c:\path\to\myenv`

### Activate the environment:

Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. The invocation of the script is platform-specific (<venv> must be replaced by the path of the directory containing the virtual environment):

Command to activate virtual environment

#### POSIX

> bash/zsh

`$ source <venv>/bin/activate`

> fish

`$ . <venv>/bin/activate.fish`

> csh/tcsh

`$ source <venv>/bin/activate.csh`

> PowerShell Core

`$ <venv>/bin/Activate.ps1`

#### Windows

> cmd.exe

`<venv>\Scripts\activate.bat`

> PowerShell

`<venv>\Scripts\Activate.ps1`

### Installing Dependencies:

After activating virtual environment run the following command to install dependencies.

`pip install -r requirements.txt`

After successful installation run the following command:

`python manage.py migrate`

## How to run:

For running the server use the following command:

`python manage.py runserver`
