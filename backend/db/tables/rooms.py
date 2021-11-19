class Room:
    def __init__(self, place, address, is_full=False):
        self.place = place
        self.address = address

        self.is_full = is_full

    def to_json(self):
        return {"place": self.place, "address": self.address, "is_full": self.is_full}
