# 1. Utwórz plik .env z konfiuracją w głownym katalogu
e.g. showapp/.env

    FLASK_DEBUG=True
    FLASK_APP=core
    SECRET_KEY=adsdsasaddadadsasaddsadadasda
    SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    RECAPTCHA_PUBLIC_KEY=xyz
    RECAPTCHA_PRIVATE_KEY=xyz

# 2 Będziesz potrzebował PIPENV
    https://pypi.org/project/pipenv/
    pip install pipenv

# 3. Uruchom pipenv

    pipenv shell

# 4. SYNC pypi 

    pipenv sync

# 5 Utwórz DB

    flask db upgrade

# 6. uruchom lokalnie

    python3 run.py


# 7. Korzystaj z localhost:5000 aby sprawdzić działanie recaptcha

    localhost:5000