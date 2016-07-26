'''
Created on 25 lug 2016

@author: lorenzo
'''

import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/poxdna.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(24)
    
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    
    POXDNA_TITLE = "poxDNA - An oxDNA webapp"
    
class DebugConfig(Config):
    DEBUG = True
    SECURITY_CONFIRMABLE = False
    