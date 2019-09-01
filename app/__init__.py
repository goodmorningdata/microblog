from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''
The Flask-Login extension manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. It also provides the "remember me" functionality that allows users to remain logged in even after closing the browser window. Requires certain properties and methods to be implemented in the user model - is_authenticated, is_active, is_anonymous, get_id(). Generic implementations included in mixin class, UserMixin.
'''
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
