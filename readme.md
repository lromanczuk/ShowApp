# 1. Utwórz plik .env z konfiuracją

.env sample

    FLASK_DEBUG=True
    FLASK_APP=core
    SECRET_KEY=adsdsasaddadadsasaddsadadasda
    SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    RECAPTCHA_PUBLIC_KEY=xyz
    RECAPTCHA_PRIVATE_KEY=xyz

# 2. Utwórz DB

    flask db upgrade

# 3. uruchom lokalnie

    python3 run.py

