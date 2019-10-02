from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS
from config import *

app = Flask(__name__)
app.config.from_object(Config())
CORS(app)

mysql = MySQL(app)
