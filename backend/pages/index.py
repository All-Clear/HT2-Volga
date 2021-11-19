from db.manager_db import db
from flask import Blueprint

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["SELECT"])
def index_select():
    return []


@blueprint.route("/", methods=["GET", "POST"])
def index():
    return {"result": list(db["rooms"].find())}


@blueprint.route("/sort", methods=["SELECT"])
def sort_select():
    return []


@blueprint.route("/sort", methods=["GET", "POST"])
def sort():
    return {"result": list(db["rooms"].find())}

