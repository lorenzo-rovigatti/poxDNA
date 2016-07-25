'''
Created on 26 Jul 2016

@author: rovigattil
'''

__all__ = ["user", ]

from flask_sqlalchemy import SQLAlchemy
# Create database connection object
db = SQLAlchemy()

def initialise_db(user_datastore):
    db.create_all()
    import user
    user.init(user_datastore)
    
    db.session.commit()