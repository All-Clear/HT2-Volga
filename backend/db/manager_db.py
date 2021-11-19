from pymongo import MongoClient
from config import MongoDB_URL

clint_db = MongoClient(MongoDB_URL)
db = clint_db["rooms"]
