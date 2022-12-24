<!-- this piece of documentation assumes windows 11 as the developer platform, see ian lisien or or whoever is currently the lead web developer for compatability concerns-->
# Windows 11 Developer Environment Setup
- basic setup
    - install the latest version of visual studio code, follow set up instructions for wsl, with ubuntu 20.04 distro
    - clone into `~/` from `github.com/ilisien/the-dorsal`
    - run `sudo apt-get update`
    - install venv with `sudo apt install python3.10-venv` (replace 3.10 with your python version)
    - navigate to the project folder at `~/the-dorsal` using `cd ~/the-dorsal/dorsal`
    - initiate a virtual environment with `python -m venv env` 
    - activate the virtual environment with `source env/bin/activate`
    - install requirements with `pip install -r requirements.txt` from inside the `~/the-dorsal` folder created by cloning in the previous step
    - run the `gen_txts.py` file, to set up the `secrets.txt` and `allowed_hosts.txt` files
    - add any additional desired hosts to `allowed_hosts.txt`
- steps to run
    - compile scss into css with the watch command: `python manage.py sass static/scss/ static/css/ --watch`
    - run the development server with `python manage.py runserver`
