from dotenv import dotenv_values, load_dotenv
from datetime import timedelta
import os

load_dotenv()

class Config(object):
    # app
    FLASK_APP = os.environ.get('FLASK_APP', 'core')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False') # must be a string
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    # db
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') 
    # static files
    SEND_FILE_MAX_AGE_DEFAULT=timedelta(hours=12)
    # captcha 
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') 
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') 
