from flask import Flask, redirect, url_for
from flaskext.mysql import MySQL
from flask_restplus import Api
from src import app

api = Api(app)

from src.streams import api as streams_api

api.add_namespace(streams_api)

if __name__ == '__main__':
    app.run(debug=True)
