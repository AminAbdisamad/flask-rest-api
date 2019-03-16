import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Setup basedir

apps = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# Database
apps.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sql')
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(apps)
mm = Marshmallow(apps)
