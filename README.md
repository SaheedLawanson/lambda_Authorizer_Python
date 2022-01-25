# lambda_Authorizer_python

## About the project
This project is a script from AWS Lambda written in NodeJS and it's function is to authorize JWT tokens (HS256) passed in a URL header

## Usage
This script is meant to be run in AWS lambda IDE and the following steps need to be taken to set it up properly:
- Open up CMD in the project root directory
- run ```pip install virtualEnv``` (If you don't have the virtual env module)
- Create a virtual environment named "venv" ```python -m venv venv```
- run ```pip install requirements.txt``` to install all dependencies
- create a new folder called "my-deployment-package" in the project root
- navigate to "path/to/the/project/root/venv/Lib/site-packages
- copy all the files in the site-packages folder and the lambda_function.py script to my-deployment-package
- compress "my-deployment-package" and upload to AWS lambda

