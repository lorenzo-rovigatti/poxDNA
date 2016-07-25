'''
Created on 25 lug 2016

@author: lorenzo
'''

from flask import Flask, render_template
from flask_security import Security, SQLAlchemyUserDatastore, login_required

# Create app
app = Flask(__name__)
app.config.from_object("config.DebugConfig")
app.debug = app.config['DEBUG']

from models import db, user

db.init_app(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, user.User, user.Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def initialise_db():
    from sqlalchemy_utils import database_exists
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']): 
        from models import initialise_db
        initialise_db(user_datastore)

# Views
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/projects")
@login_required
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run()
    