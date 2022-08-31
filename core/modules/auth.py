import imp
from flask import Blueprint, redirect, render_template, request, url_for, flash
from core.forms.auth import LogInForm, SignUpForm
from flask_login import login_user, logout_user
from core.helpers.create_user import create_user
from core.helpers.captcha import is_human
from core.models import Tags
from core.helpers.auth_decorators import for_anonymous
from core import models
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)

@auth.get('/')
@auth.post('/')
@for_anonymous
def login():
    form = LogInForm()
    if form.validate_on_submit() and is_human(request.form['g-recaptcha-response']):
        user = models.User.query.filter_by(email=form.email.data).first() 
        if user and check_password_hash(user.password, form.password.data): 
            login_user(user, remember=True)
            return redirect(url_for('panel.main')) 
        else:
            flash('Takie konto nie istnieje lub jest zablokowane', 'error')
    return render_template('auth/login.html', form=form)

@auth.get('/signup')
@auth.post('/signup')
@for_anonymous
def register():
    form = SignUpForm()
    if form.validate_on_submit() and is_human(request.form['g-recaptcha-response']):
        if create_user(form.email.data, form.password1.data, [Tags.USER]):
            return redirect(url_for('panel.main'))
    return render_template('auth/register.html', form=form)

# @auth.get('/register')
# @auth.post('/register')
# def register():
#     form = LogInForm()
# print(crete_user('1', '2', '3', []))
#     return render_template('auth/register.html', form=form)

@auth.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))