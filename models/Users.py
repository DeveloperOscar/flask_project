from datetime import datetime
from utils.db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable= False, unique = True)
    data_added = db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self):
        return '<Name %r>'% self.name
