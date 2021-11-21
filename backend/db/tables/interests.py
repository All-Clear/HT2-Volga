from bson.objectid import ObjectId
from typing import Tuple


class Interest:
    def __init__(self, id: ObjectId, id_interest: int, id_tenant: ObjectId):
        self.id = id
        self.id_interest = id_interest

        self.id_tenant = id_tenant

    @staticmethod
    def from_db(**kwargs):
        return Interest(kwargs["_id"], kwargs["id_interest"], kwargs["id_tenant"])

    def to_db(self) -> Tuple[ObjectId, dict]:
        return self.id, {"id_interest": self.id_interest, "id_tenant": self.id_tenant}

    def to_text(self) -> str:
        list_name = ["BAD", "Наука", "Политика", "Спорт", "Другое"]
        if len(list_name) < self.id_interest:
            return f"no name ({self.id_interest})"
        else:
            return list_name[self.id_interest]