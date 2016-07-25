'''
Created on 25 lug 2016

@author: lorenzo
'''

import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = os.urandom(24)
    SECURITY_LOGIN_USER_TEMPLATE = "user/login.html"
    
class DebugConfig(Config):
    DEBUG=True
    