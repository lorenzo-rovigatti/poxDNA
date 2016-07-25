'''
Created on 25 Jul 2016

@author: rovigattil
'''

from models import db

projects_users = db.Table('projects_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('project_id', db.Integer(), db.ForeignKey('project.id')))

class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    