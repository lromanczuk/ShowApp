from time import sleep
from flask import Blueprint, redirect, render_template, make_response, request, url_for, flash
from core.helpers.auth_decorators import for_verified

panel = Blueprint('panel', __name__)

@panel.get('/')
@for_verified
def main():
    return render_template('panel/main.html')

@panel.get('/training')
@for_verified
def training():
    return 'training'

@panel.get('/meals')
@for_verified
def meals():
    return 'Meals'