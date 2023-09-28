import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import env if it's there (local use, not on github)
if os.path.exists("env.py"):
    import env


# create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create an instance of the SQLAlchemy class and set to the instance of the Flask app
db = SQLAlchemy(app)

# this need app and db to be imported
from taskmanager import routes