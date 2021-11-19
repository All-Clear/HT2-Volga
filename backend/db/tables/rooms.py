from bson.objectid import ObjectId
from ..manager_db import db
from .tenants import Tenant

from typing import List


class Room:
    def __init__(self, id: ObjectId, type_room: int, cur_count_passengers: int, max_count_passenger: int,
                 tenants: List[ObjectId], place: int, address: int, is_free=True):
        self.id = id

        self.type_room = type_room

        self.cur_count_passengers = cur_count_passengers
        self.max_count_passenger = max_count_passenger

        self.tenants = tenants

        self.is_free = is_free

        self.address = address
        self.place = place

    def add_tenant(self, new_tenants: ObjectId):
        self.cur_count_passengers += 1
        self.tenants.append(new_tenants)

        if self.type_room == 0:
            if self.cur_count_passengers == self.max_count_passenger:
                self.is_free = False

    @staticmethod
    def from_db(**kwargs):
        return Room(kwargs["_id"], kwargs["type_room"], kwargs["cur_count_tenants"], kwargs["max_count_tenants"],
                    kwargs["tenants"], kwargs["is_free"], kwargs["address"], kwargs["place"])

    def to_db(self):
        return self.id, {"is_free": self.is_free,
                         "max_count_tenants": self.max_count_passenger,
                         "cur_count_tenants": self.cur_count_passengers,
                         "type_room": self.type_room,
                         "tenants": [tenants for tenants in self.tenants],
                         "address": self.address,
                         "place": self.place}

    def to_json(self) -> dict:
        return {"id_room": str(self.id),
                "is_free": self.is_free,
                "max_count_tenants": self.max_count_passenger,
                "cur_count_tenants": self.cur_count_passengers,
                "type_room": self.type_room,
                "tenants": [Tenant.from_db(**(db["interests"].find_one({"_id": tenants}))).to_json() for tenants in
                            self.tenants],
                "address": self.address,
                "place": self.place}
