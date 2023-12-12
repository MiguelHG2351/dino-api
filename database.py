from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
import os
from pymongo.server_api import ServerApi
from models import DinoCollection

print(os.getenv('DATABASE_URL'))
client = AsyncIOMotorClient(os.getenv('DATABASE_URL'))
database = client.get_database('dinoDB')

collection = database.get_collection('dinos')

print(dir(collection))


async def get_all_dinos():
    return DinoCollection(dinos = await collection.find().to_list(100))


async def get_one_dino_id(id):
    dinos = await collection.find_one({"_id": ObjectId(id)})
    return dinos
