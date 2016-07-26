'''
Created on 25 Jul 2016

@author: rovigattil
'''

from flask_security import UserMixin, RoleMixin
from models import db
from project import projects_users

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
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
    
def init(datastore):
    adm_role = datastore.create_role(name="admin", description="The administrator")
    user_role = datastore.create_role(name="user", description="A regular user")
    
    adm_user = datastore.create_user(email='lorenzo.rovigatti@gmail.com', password='nicepwd')
    user_user = datastore.create_user(email='lorenzo.rovigatti2@physics.ox.ac.uk', password='nicepwd')
    
    datastore.add_role_to_user(adm_user, adm_role)
    datastore.add_role_to_user(user_user, user_role)
    
