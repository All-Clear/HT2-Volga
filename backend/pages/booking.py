from db.tables.interests import Interest
from flask import Blueprint, request
from db.tables.tenants import Tenant
from db.tables.rooms import Room
from db.manager_db import db
from bson import ObjectId

blueprint = Blueprint("booking", __name__)


@blueprint.route("/booking", methods=["OPTIONS"])
def booking_options():
    return {}


@blueprint.route("/booking", methods=["POST"])
def booking():
    json_data = request.get_json()
    print(json_data)

    room = Room.from_db(**db["rooms"].find_one({"_id": ObjectId(json_data["id_room"])}))

    json_data["_id"] = "None"
    json_data["desire_communicate"] = json_data["communication"]
    json_data["vaccination_against_covid19"] = json_data["hasGraft"]
    json_data["interests"] = []

    json_data["place_in_address"] = room.address

    list_interest = [i for i in range(1, len(json_data["preferences"]) + 1) if json_data["preferences"][str(i)]]

    del json_data["communication"]
    del json_data["hasGraft"]
    del json_data["preferences"]

    tenant = Tenant.from_db(**json_data)
    tenant_id = db["tenants"].insert_one(tenant.to_db()[1]).inserted_id

    for type_interest in list_interest:
        interest = Interest("None", type_interest, tenant_id)
        interest_id = db["interests"].insert_one(interest.to_db()[1]).inserted_id
        tenant.interests.append(interest_id)

    db["tenants"].update_one({"_id": tenant_id}, {"$set": {"interests": tenant.interests}})

    room.add_tenant(tenant_id)
    db["rooms"].update_one({"_id": room.id}, {"$set": {"tenants": room.tenants, "is_free": room.is_free}})

    return {}