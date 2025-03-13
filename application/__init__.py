#Creator: Israel Showell
#Date: 3/12/2025
#Purpose: This is a test file to test the Flask framework.



from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.app_context()

#We set these configurations for security purposes

#This tells us the name of the database we are using
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'

#This tells us what our secret key is for the application is
#This prevents cross-site request forgery attacks
app.config['SECRET_KEY'] = 'jfIH*re3n290djNMDj0myaibd23'

db = SQLAlchemy(app)

from application import routes