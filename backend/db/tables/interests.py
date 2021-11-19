from bson.objectid import ObjectId
from typing import Tuple


class Interest:
    def __init__(self, id: ObjectId, id_interest: int):
        self.id = id
        self.id_interest = id_interest

    @staticmethod
    def from_db(**kwargs):
        return Interest(kwargs["_id"], kwargs["id_interest"])

    def to_db(self) -> Tuple[ObjectId, dict]:
        return self.id, {"id_interest": self.id_interest}

    def to_text(self) -> str:
        list_name = ["BAD", "Наука", "Искуство", "Спорт", "Другое"]
        if len(list_name) < self.id_interest:
            return f"no name ({self.id_interest})"
        else:
            return list_name[self.id_interest]