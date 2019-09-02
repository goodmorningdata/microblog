import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Use a class to store configuration variables.
class Config(object):
    # SECRET_KEY used by the Flask-WTF extension to protect web forms
    # against Cross-Site Requet Forgery (CSRF) attacks.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3

    # Email server details.
    # Test mail server is not working - FIX THIS!
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['goodmorningdata@gmail.com']
