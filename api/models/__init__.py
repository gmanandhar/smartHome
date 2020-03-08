from api import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import RPi.GPIO as GPIO

#Initilized Database
basedir = os.path.abspath(os.path.dirname(__file__))
    # Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'smartHome.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#Initilized Mode
pi= GPIO
pi.setmode(GPIO.BOARD) # Select the interal board pins