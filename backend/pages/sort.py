from db.tables.rooms import Room
from db.manager_db import db
from flask import Blueprint, request
from db.tables.tenants import Tenant

blueprint = Blueprint("sort", __name__)


@blueprint.route("/sort", methods=["OPTIONS"])
def sort_select():
    return {"good_list": [], "alternative_list": []}


@blueprint.route("/sort", methods=["GET", "POST"])
def sort_get():
    json_data = request.get_json()

    list_rooms = [Room.from_db(**room) for room in db["rooms"].find({"is_free": True})]
    good_list = []
    alternative_list = []

    for room in list_rooms:
        bal_room = 0
        is_alt = False
        for tenant_id in room.tenants:
            tenant = Tenant.from_db(**db["tenants"].find_one({"_id": tenant_id}))

            # Проверяем подходит ли нам сосед
            if tenant.gender != json_data["gender"]:
                bal_room -= 100
                is_alt = True
                print(f"room address: {room.address} {str(tenant_id)} {1}")

            if json_data["neighborsAge"][0] > tenant.age or tenant.age > json_data["neighborsAge"][1] or\
                    tenant.neighborsAge[0] > json_data["age"] or json_data["age"] > tenant.neighborsAge[1]:
                is_alt = True
                print(f"room address: {room.address} {str(tenant_id)} {2}")

            if tenant.desire_communicate != json_data["communication"]:
                bal_room -= 10
            else:
                bal_room += 10

            if (json_data["neighborsHasPet"] and tenant.hasPet) or\
                    (tenant.neighborsHasPet and json_data["hasPet"]):
                is_alt = True
                bal_room -= 15
                print(f"room address: {room.address} {str(tenant_id)} {3}")

            if json_data["hasGraft"] != tenant.vaccination_against_covid19:
                is_alt = True
                bal_room -= 15
                print(f"room address: {room.address} {str(tenant_id)} {4}")

            if (json_data["neighborsHasChild"] and tenant.hasChild) or\
                    (tenant.neighborsHasChild and json_data["hasChild"]):
                is_alt = True
                bal_room -= 15
                print(f"room address: {room.address} {str(tenant_id)} {5}")

            if (json_data["neighborsSmoking"] and tenant.smoking) or (tenant.neighborsSmoking and json_data["smoking"]):
                is_alt = True
                bal_room -= 15
                print(f"room address: {room.address} {str(tenant_id)} {6}")

            tenant_interests = [db["interests"].find_one({"_id": interest})["id_interest"] for interest in tenant.interests]

            if json_data["preferences"]["1"] == 1 in tenant_interests:
                bal_room += 5
            if json_data["preferences"]["2"] == 2 in tenant_interests:
                bal_room += 5
            if json_data["preferences"]["3"] == 3 in tenant_interests:
                bal_room += 5
            if json_data["preferences"]["4"] == 4 in tenant_interests:
                bal_room += 5

        if is_alt:
            alternative_list.append((bal_room, room))
        else:
            good_list.append((bal_room, room))

    good_list.sort(key=lambda x: x[0], reverse=True)
    alternative_list.sort(key=lambda x: x[0], reverse=True)
    print(good_list)
    return {"good_list": [room.to_json() for bal, room in good_list],
            "alternative_list": [room.to_json() for bal, room in alternative_list]}
