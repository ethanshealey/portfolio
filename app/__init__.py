from flask import Flask
from config import Config
from flask_mail import Mail

app = Flask(__name__, static_url_path='/', static_folder='/')
app.config.from_object(Config)
mail = Mail(app)

from app import routes