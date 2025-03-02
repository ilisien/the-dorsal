# The Dorsal Webpage
Hi!  
This is the repository for the Dorsal's webpage! Interested in helping out? See environment setup below!

# Wagtail Project Setup Guide

This guide will help you set up the [the-dorsal](https://github.com/ilisien/the-dorsal) repository on your local machine, including cloning the repository, setting up Python, creating a virtual environment, installing dependencies, configuring PostgreSQL, and running the Wagtail development server.

## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- **Git**: [Download Git](https://git-scm.com/downloads)
- **Python** (latest version): [Download Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Download PostgreSQL](https://www.postgresql.org/download/)

---

## 1. Clone the Repository

### Linux/macOS
```bash
# Open a terminal and run:
git clone https://github.com/ilisien/the-dorsal.git
cd the-dorsal
```

### Windows (Git Bash/Command Prompt)
```bash
git clone https://github.com/ilisien/the-dorsal.git
cd the-dorsal
```

---

## 2. Set Up Python and Virtual Environment

### Linux/macOS
```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate
```

### Windows (Command Prompt)
```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
env\Scripts\activate
```

### Windows (PowerShell)
```powershell
# Create a virtual environment
python -m venv env

# Activate the virtual environment
.env\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

Once the virtual environment is activated, install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## 4. Install and Configure PostgreSQL

### Linux/macOS
1. Install PostgreSQL:
   ```bash
   sudo apt install postgresql  # Ubuntu/Debian
   brew install postgresql      # macOS (using Homebrew)
   ```
2. Start the PostgreSQL service:
   ```bash
   sudo service postgresql start  # Ubuntu/Debian
   brew services start postgresql # macOS
   ```
3. Open the PostgreSQL shell:
   ```bash
   sudo -u postgres psql
   ```

### Windows
1. Download and install PostgreSQL from [here](https://www.postgresql.org/download/).
2. Open **pgAdmin** or the **SQL Shell (psql)**.
3. In the shell, run:
   ```sql
   CREATE DATABASE thedorsal;
   CREATE USER thedorsaluser WITH PASSWORD 'insert secure password here';
   GRANT ALL PRIVILEGES ON DATABASE thedorsal TO thedorsaluser;
   ```

---

## 5. Configure Django Settings

1. Create a file named `postgres_password.txt` in the `dorsal/dorsal/` folder -- insert your newly created PostgreSQL password.

2. Run the automatic secret generator `gen_txts.py` using:
   ```bash
   python gen_txts.py
   ```

---

## 6. Run Database Migrations

Apply migrations to set up the database schema:
```bash
python manage.py migrate
```

---

## 7. Create a Superuser

To access the admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

---

## 8. Run the Development Server

Start the server with:
```bash
python manage.py runserver
```

By default, the server will be accessible at:
```
http://127.0.0.1:8000/
```

To access the Wagtail admin panel, go to:
```
http://127.0.0.1:8000/admin
```
Log in with the superuser credentials you created earlier.

---

## Troubleshooting

I won't be so condescending as to include the ChatGPT'd troubleshooting guide -- if you need help please feel free to email me at ilisien@outlook.com even if I'm in college.

