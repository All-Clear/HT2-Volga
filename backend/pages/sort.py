from db.manager_db import db
from flask import Blueprint

blueprint = Blueprint("sort", __name__)


@blueprint.route("/sort", methods=["SELECT"])
def sort_select():
    return []


@blueprint.route("/sort", methods=["GET"])
def sort_get():
    data = db["rooms"].find()
    result = []
    for item in data:
        del item["_id"]
        result.append(item)
    return {"result": result}
