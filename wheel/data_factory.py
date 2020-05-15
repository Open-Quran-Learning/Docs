from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import ayat.models as model
import os

model.app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/postgres"
#model.app.config["SQLALCHEMY_DATABASE_URI"] = "<your local database link>"
model.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



