'''
Created on 26 Jul 2016

@author: rovigattil
'''

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.ext.sqlalchemy.orm import model_form
from models import Project, Task
from app import db

ProjectForm = model_form(Project, base_class=Form, db_session=db.session)
TaskForm = model_form(Task, base_class=Form, db_session=db.session)
