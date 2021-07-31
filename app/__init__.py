from flask import Flask
from flask_sqlalchemy import SQLAlchemy, ForeignKey
from flask_potion import ModelResource, fields

app = Flask(__name__)
db = SQLAlchemy(app)
