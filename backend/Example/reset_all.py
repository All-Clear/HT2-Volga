from db.manager_db import db

for col in db.list_collection_names():
    db[col].delete_many({})