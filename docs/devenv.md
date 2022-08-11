# setting up a developer environment
follow the steps for your operating system
if your os is not listed, or you are having issues: contact the lead developer or create a github issue report

### development on ubuntu setup
- clone or pull from github
- create virtual environment with python in the `dorsal/env` directory with `$ python3 -m venv env` after navigating to the `dorsal/` directory
- activate virtual environment with `$ source env/bin/activate`
- install dependencies with `(env) $ pip install -r requirements.txt`

- start development server and watch scss changes with `(env) $ python manage.py runserver & python manage.py sass-compiler --watch`