'''
Created on 25 lug 2016

@author: lorenzo
'''

from flask import Flask, render_template
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_security.core import current_user
from flask_mail import Mail

# Create app
app = Flask(__name__)
app.config.from_object("config.DebugConfig")
app.debug = app.config['DEBUG']
mail = Mail(app)

from models import db, user, project

db.init_app(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, user.User, user.Role)
security = Security(app, user_datastore)


@app.before_first_request
def initialise_db():
    from sqlalchemy_utils import database_exists
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']): 
        from models import initialise_db
        initialise_db(user_datastore)

# Views
@app.route('/')
def home():
    return render_template('new_index.html')

@app.route("/projects")
@login_required
def projects():
    from models.project import Project
    from models.user import User
    
    projects = User.query.filter_by(id=current_user.get_id()).first().projects
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run()
    