from bson.objectid import ObjectId
from .interests import Interest
from ..manager_db import db
from typing import List, Tuple


class Tenant:
    def __init__(self, id: ObjectId, place_in_address: int, place_in_room: int, gender: bool, age: int,
                 desire_communicate: bool, vaccination_against_covid19: bool, hasPet: bool, hasChild: bool,
                 smoking: bool, interests: List[ObjectId]):
        self.id = id
        self.place_in_address = place_in_address
        self.place_in_room = place_in_room
        self.gender = gender
        self.age = age
        self.desire_communicate = desire_communicate
        self.vaccination_against_covid19 = vaccination_against_covid19
        self.hasPet = hasPet
        self.hasChild = hasChild
        self.smoking = smoking

        self.interests = interests

    @staticmethod
    def from_db(**kwargs):
        return Tenant(kwargs["_id"], kwargs["place_in_address"], kwargs["place_in_room"], kwargs["gender"],
                      kwargs["age"], kwargs["desire_communicate"], kwargs["vaccination_against_covid19"],
                      kwargs["hasPet"], kwargs["hasChild"], kwargs["smoking"], kwargs["interests"])

    def to_db(self) -> Tuple[ObjectId, dict]:
        return self.id, {"place_in_address": self.place_in_address,
                         "place_in_room": self.place_in_room,
                         "gender": self.gender,
                         "age": self.age,
                         "interests": self.interests,
                         "desire_communicate": self.desire_communicate,
                         "vaccination_against_covid19": self.vaccination_against_covid19,
                         "hasPet": self.hasPet,
                         "hasChild": self.hasChild,
                         "smoking": self.smoking}

    def to_json(self) -> dict:
        return {"id": str(self.id),
                "place_in_address": self.place_in_address,
                "place_in_room": self.place_in_room,
                "gender": self.gender,
                "age": self.age,
                "interests": [Interest.from_db(**(db["interests"].find_one({"_id": interest}))).to_text() for interest in self.interests],
                "desire_communicate": self.desire_communicate,
                "vaccination_against_covid19": self.vaccination_against_covid19,
                "hasPet": self.hasPet,
                "hasChild": self.hasChild,
                "smoking": self.smoking}
