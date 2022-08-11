<!-- updated aug 10th 2022 by ian lisien -->
<!-- this piece of documentation asssumes Ubuntu 22.04 as the development platform, see ian lisien or whoever is currently the lead web developer for compatability concerns-->
# initialization of django environment
- create "dorsal" directory
- install django with `$ pip install django`
- create skeleton django project with `$ django-admin startproject dorsal`
- create virtual environment named `env` with `$ python3 -m venv env` while in the new "dorsal" directory
- acivate virtual environment with `$ source env/bin/activate`
- install django in the venv with `(env) $ pip install django`
- create initial migrations with `(env) $ python manage.py migrate`
- create initial superuser with `(env) $ python manage.py createsuperuser`, fill out information
- check that django is working properly with `(env) $ python manage.py runserver`, check 127.0.0.1:8000, try to login to 127.0.0.1:8000/admin

# sass setup
- install `django-sass-compiler` with `(env) $ pip install django-sass-compiler`
- run `(env) $ python manage.py sass-compiler --watch` to watch for changes in static .scss files, convert to .css 