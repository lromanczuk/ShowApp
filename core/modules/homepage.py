from flask import Blueprint, redirect, render_template, make_response, request, url_for
import datetime

homepage = Blueprint('homepage', __name__)

@homepage.get('/')
def home():
    return render_template('homepage/home.html')

@homepage.get('/cookies')
def cookies():
    # get cookie
    cookie_info = request.cookies.get('cookie_info')
    # return nothing if cookie info is set to no
    if cookie_info == 'no':
        return ''
    # create response
    resp = make_response(render_template('homepage/cookies.html'))
    if cookie_info != 'no':
        # cookie expire date
        expire_date = datetime.datetime.now() + datetime.timedelta(days=360)
        # add cookie 
        resp.set_cookie('cookie_info', 'yes', expires=expire_date)
    return resp

@homepage.get('/cookies_info')
def cookies_info():
    expire_date = datetime.datetime.now() + datetime.timedelta(days=360)
    resp = make_response(redirect(url_for('homepage.cookies')))
    resp.set_cookie('cookie_info', 'no', expires=expire_date)
    return resp


@homepage.get('/flashs')
def flashs():
    return render_template('flash.html')