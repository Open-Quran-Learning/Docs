from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  "postgres://postgres:root@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import ayat.models



