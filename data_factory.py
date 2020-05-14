from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import ayat_model as ayat
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#ayat.teardown_db() 
ayat.setup_db()

