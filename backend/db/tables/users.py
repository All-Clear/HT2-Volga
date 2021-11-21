from bson.objectid import ObjectId


class User:
    def __init__(self, id: ObjectId, phone: str, email: str, password: str, gender: bool, age: int,
                 desire_communicate: bool, vaccination_against_covid19: bool, hasPet: bool, hasChild: bool,
                 smoking: bool):
        self.id = id
        self.phone = phone
        self.email = email
        self.password = password
        self.gender = gender
        self.age = age
        self.desire_communicate = desire_communicate
        self.vaccination_against_covid19 = vaccination_against_covid19
        self.hasPet = hasPet
        self.hasChild = hasChild
        self.smoking = smoking
