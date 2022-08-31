from flask import Blueprint, redirect, render_template, make_response, request, url_for, flash
from core.helpers.auth_decorators import for_verified
from flask_login import current_user
from core.forms.panel import ChangePasswordForm
from werkzeug.security import check_password_hash, generate_password_hash
from core import db, models

settings = Blueprint('settings', __name__)

@settings.get('/')
@for_verified
def menu():
    return render_template('panel/settings/settings.html')

@settings.get('/change_password')
@settings.post('/change_password')
@for_verified
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.current_password.data):
            # change password
            current_user.password = generate_password_hash(form.password1.data)
            db.session.commit()
            flash('Twoje hasło zostało zmienione', 'success')
            return redirect(url_for('settings.menu'))
        else:
            flash('Podałeś złe hasło! Twoje hasło nie zostało zmienione', 'error')

    return render_template('panel/settings/change_password.html', form=form)