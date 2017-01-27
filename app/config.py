import os

class Configuration(object):
    APPLICATION_DIR =  os.path.dirname(os.path.realpath(__file__)) 
    
    DEBUG=True

    SQLALCHEMY_DATABASE_URI = 'mysql://flaskuser:manish12@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    