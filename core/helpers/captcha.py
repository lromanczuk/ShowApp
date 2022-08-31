from core import Config
import requests

def get_recaptcha_public_key():
    return Config.RECAPTCHA_PUBLIC_KEY

def is_human(response_captcha):
    '''
    Function returns True if captcha is valid
    '''
    URL_GOOGLE_VERIFY = 'https://www.google.com/recaptcha/api/siteverify'
    r = requests.post(url=f'{URL_GOOGLE_VERIFY}?secret={Config.RECAPTCHA_PRIVATE_KEY}&response={response_captcha}')
    status = r.json()['success']
    return status