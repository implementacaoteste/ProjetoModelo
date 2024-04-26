# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

# from config import app_config, app_active

# config = app_config[app_active]
# db = SQLAlchemy(config.APP)

#from app import db
from .shared import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
