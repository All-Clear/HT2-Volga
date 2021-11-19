from flask import Flask
from db.manager_db import db

app = Flask(__name__)

app.config.from_pyfile("config.py")

db.init_app(app)
with app.app_context():
    db.create_all()


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True

    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, PATCH, DELETE, POST, PUT'

    response.headers['Access-Control-Allow-Headers'] = "Access-Control-Allow-Headers, Origin,Accept, " \
                                                       "X-Requested-With, Content-Type, " \
                                                       "Access-Control-Request-Method, Access-Control-Request-Headers"

    return response
