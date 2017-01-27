from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from config  import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

api = APIManager(app,flask_sqlalchemy_db=db)






    



