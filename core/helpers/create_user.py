from core import models
from flask import flash
from werkzeug.security import generate_password_hash
from core import db
from flask_login import login_user

def create_user(email: str, password: str, tags: list):
    # account is exist?
    account = models.User.query.filter_by(email=email.lower()).first()
    
    ## No
    if not account:
        # create user
        u = models.User(email=email, password=generate_password_hash(password))
        db.session.add(u)
        db.session.commit()
        # add tags
        for tag in tags:
            new_tag = models.Tag(user_id=u.id, value=tag)
            db.session.add(new_tag)
        db.session.commit()
        flash('Konto zostało utworzone', 'success')
        login_user(u, remember=True)
        return True

    ## Yes
    else:
        flash('Konto już istnieje lub zostało zablokowane', 'error')
        return False


    