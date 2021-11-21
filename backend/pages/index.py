from flask import Blueprint, request
from db.manager_db import db
from db.tables.rooms import Room

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["OPTIONS"])
def index_select():
    return {"result": []}


@blueprint.route("/", methods=["GET"])
def index_get():
    return {"result": [Room.from_db(**room).to_json() for room in db["rooms"].find()]}


@blueprint.route("/", methods=["POST"])
def index_post():
    json_data = request.get_json()
    room = Room(**json_data)

    db["rooms"].insert_one(room.to_db()[1])
    return {}
