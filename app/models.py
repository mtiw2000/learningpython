import datetime, re

from app import db


def slugify(s):
    return re.sub('[^\w]+','-',s).lower()
    
class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    
    
    
    
    
