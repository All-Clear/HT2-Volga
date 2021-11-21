from db.tables.interests import Interest
from flask import Blueprint, request
from db.tables.tenants import Tenant
from db.tables.rooms import Room
from db.manager_db import db

blueprint = Blueprint("add", __name__)


@blueprint.route("/add/room", methods=["OPTIONS"])
def add_room_options():
    return {}


@blueprint.route("/add/room", methods=["POST"])
def add_room():
    json_data = request.get_json()
    room = Room(**json_data)

    db["rooms"].insert_one(room.to_db()[1])
    return {}


@blueprint.route("/add/user", methods=["OPTIONS"])
def add_user_options():
    pass


@blueprint.route("/add/user", methods=["POST"])
def add_user():
    pass


@blueprint.route("/add/tenant", methods=["OPTIONS"])
def add_tenant_options():
    return {}


@blueprint.route("/add/tenant", methods=["POST"])
def add_tenant():
    json_data = request.get_json()

    interests = json_data["interests"].copy()
    json_data["interests"] = []

    tenant = Tenant(**json_data)
    tenant_id = db["tenants"].insert_one(tenant.to_db()[1]).inserted_id

    for interest_type in interests:
        interest = Interest("None", interest_type, tenant_id)
        interest_id = db["interests"].insert_one(interest.to_db()[1]).inserted_id
        tenant.interests.append(interest_id)
    print(tenant_id)
    db["tenants"].update_one({"_id": tenant_id}, {"$set": {"interests": tenant.interests}})

    room = Room.from_db(**db["rooms"].find_one({"address": tenant.place_in_address}))
    room.add_tenant(tenant_id)

    db["rooms"].update_one({"_id": room.id}, {"$set": {"tenants": room.tenants}})
    return {}