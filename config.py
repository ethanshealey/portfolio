import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'homemadedub@gmail.com'
    MAIL_PASSWORD = 'mnpdapcxrvnlcclb'
    ADMINS = ['ethan.shealey@gmail.com']