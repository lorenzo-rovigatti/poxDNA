# -*- coding: utf-8 -*-
'''
Created on 26 Jul 2016

@author: rovigattil
'''

from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

# Create database connection object
db = SQLAlchemy()

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


projects_users = db.Table('projects_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('project_id', db.Integer(), db.ForeignKey('project.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(15))
    current_login_ip = db.Column(db.String(15))
    login_count = db.Column(db.Integer)
    
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('user', lazy='dynamic'))
    projects = db.relationship('Project', secondary=projects_users, backref=db.backref('project', lazy='dynamic'))
    
    
class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text())
    
    users = db.relationship('User', secondary=projects_users, backref=db.backref('user', lazy='dynamic'))
    tasks = db.relationship('Task', backref=db.backref('project'))
    
    def __init__(self, title="", description=""):
        self.title = title
        self.description = description
        
        
class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text())
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    tasktype_id = db.Column(db.Integer, db.ForeignKey('task_type.id'))


class TaskType(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text())

    tasks = db.relationship('Task', backref=db.backref('task_type'))
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    
def initialise_db(datastore):
    db.create_all()
    
    adm_role = datastore.create_role(name="admin", description="The administrator")
    user_role = datastore.create_role(name="user", description="A regular user")
    
    adm_user = datastore.create_user(email='lorenzo.rovigatti@gmail.com', password='nicepwd')
    user_user = datastore.create_user(email='lorenzo.rovigatti2@physics.ox.ac.uk', password='nicepwd')
    
    datastore.add_role_to_user(adm_user, adm_role)
    datastore.add_role_to_user(user_user, user_role)
    
    project = Project("Progetto di prova", u"Questo progetto è fantastico. Nulla da dire.")
    project.users.append(adm_user)
    db.session.add(project)
    
    tt = TaskType("Convert from cadnano", "Convert a cadnano file to an oxDNA initial configuration")
    db.session.add(tt)
    
    db.session.commit()
    