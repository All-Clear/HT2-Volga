from flask import Flask

from pages import booking
from pages import index
from pages import sort
from pages import add

app = Flask(__name__)

app.config.from_pyfile("./config.py")

app.register_blueprint(booking.blueprint)
app.register_blueprint(index.blueprint)
app.register_blueprint(sort.blueprint)
app.register_blueprint(add.blueprint)


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True

    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, PATCH, DELETE, POST, PUT'

    response.headers['Access-Control-Allow-Headers'] = "Access-Control-Allow-Headers, Origin,Accept, " \
                                                       "X-Requested-With, Content-Type, " \
                                                       "Access-Control-Request-Method, Access-Control-Request-Headers"

    return response
