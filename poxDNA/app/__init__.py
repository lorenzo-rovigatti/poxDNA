'''
Created on 25 lug 2016

@author: lorenzo
'''

from flask import Flask, render_template
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

# Create app
app = Flask(__name__)
app.config.from_object("config.DebugConfig")
app.debug = app.config['DEBUG']
mail = Mail(app)

from models import db, User, Project, Role
import views

db.init_app(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def initialise_db():
    from sqlalchemy_utils import database_exists
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']): 
        from models import initialise_db
        initialise_db(user_datastore)

