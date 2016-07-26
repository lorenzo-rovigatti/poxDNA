'''
Created on 26 Jul 2016

@author: rovigattil
'''

from app import app
from flask import render_template
from flask_security import login_required
from flask_security.core import current_user
from models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/projects")
@login_required
def projects():
    projects = User.query.filter_by(id=current_user.get_id()).first().projects
    return render_template('project/list.html', projects=projects)

@app.route("/project/new")
@login_required
def project_new():
    return render_template('project/new.html')