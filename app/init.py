from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager, login_manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet,configure_uploads


db =SQLAlchemy
bootstrap =Bootstrap()
login_manager =LoginManager
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)



def create_app(config_name):
    app = Flask(__name__)
    return app