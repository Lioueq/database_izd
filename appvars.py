from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7N9WLBw8?PcRuy*j2X@EdVkwyp-Y@@xk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:DaViD41933@localhost/test3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
