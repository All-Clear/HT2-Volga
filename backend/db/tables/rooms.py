from ..manager_db import db


class Room(db.Model):
    id = db.Column(db.BigInteger, primery_key=True)
