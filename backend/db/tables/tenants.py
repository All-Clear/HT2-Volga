from bson.objectid import ObjectId
from .interests import Interest
from ..manager_db import db
from typing import List, Tuple


class Tenant:
    def __init__(self, id: ObjectId, place_in_address: int, place_in_room: int, gender: bool, age: int,
                 desire_communicate: bool, vaccination_against_covid19: bool, hasPet: bool, hasChild: bool,
                 smoking: bool, interests: List[ObjectId], date_start: int, date_end: int,
                 neighborsAge: List[int], neighborsHasPet: bool, neighborsSmoking: bool, neighborsHasChild: bool):
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

        self.date_start = date_start
        self.date_end = date_end

        self.neighborsAge = neighborsAge
        self.neighborsHasPet = neighborsHasPet
        self.neighborsSmoking = neighborsSmoking
        self.neighborsHasChild = neighborsHasChild

    @staticmethod
    def from_db(**kwargs):
        return Tenant(kwargs["_id"], kwargs["place_in_address"], kwargs["place_in_room"], kwargs["gender"],
                      kwargs["age"], kwargs["desire_communicate"], kwargs["vaccination_against_covid19"],
                      kwargs["hasPet"], kwargs["hasChild"], kwargs["smoking"], kwargs["interests"],
                      kwargs["date_start"], kwargs["date_end"],
                      kwargs["neighborsAge"], kwargs["neighborsHasPet"], kwargs["neighborsSmoking"],
                      kwargs["neighborsHasChild"])

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
                         "smoking": self.smoking,
                         "date_start": self.date_start,
                         "date_end": self.date_end,
                         "neighborsAge": self.neighborsAge,
                         "neighborsHasPet": self.neighborsHasPet,
                         "neighborsSmoking": self.neighborsSmoking,
                         "neighborsHasChild": self.neighborsHasChild}

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
                "smoking": self.smoking,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "neighborsAge": self.neighborsAge,
                "neighborsHasPet": self.neighborsHasPet,
                "neighborsSmoking": self.neighborsSmoking,
                "neighborsHasChild": self.neighborsHasChild}
