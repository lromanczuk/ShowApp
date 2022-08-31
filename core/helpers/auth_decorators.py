from flask import redirect, url_for
from functools import wraps
from flask_login import current_user

def for_anonymous(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (current_user.is_authenticated):
            return redirect(url_for('panel.main'))
        return f(*args, **kwargs)
    return decorated_function

def for_verified(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not (current_user.is_authenticated):
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function