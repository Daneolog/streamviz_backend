from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'streamviz'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)
