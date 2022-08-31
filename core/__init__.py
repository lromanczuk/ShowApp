from flask import Flask, request, redirect, url_for
from core.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# app
app = Flask(__name__)
app.config.from_object(Config)

# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# csrf
# csrf = CSRFProtect(app)

# before requests actions
@app.before_request
def before_request():
    # https logic- optional http>https 
    if not request.is_secure and not Config.FLASK_DEBUG == 'True':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

# 404 handler
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('auth.login'))

# modules
from core.modules.homepage import homepage as homepage_blueprint
from core.modules.auth import auth as auth_blueprint
from core.modules.panel import panel as panel_blueprint
from core.modules.settings import settings as settings_blueprint

# register modules
app.register_blueprint(homepage_blueprint, url_prefix='/')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(panel_blueprint, url_prefix='/panel')
app.register_blueprint(settings_blueprint, url_prefix='/panel/settings')

# own jinja function
from core.helpers.captcha import get_recaptcha_public_key
app.jinja_env.globals.update(get_recaptcha_public_key=get_recaptcha_public_key)


# TODO: all files + fonts on server
# TODO: rows limit per user protect base
# TODO: google login
# TODO: checkbox on register