from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from motor.motor_asyncio import AsyncIOMotorClient
from os import getenv

class Container(DeclarativeContainer):
    db = Singleton(AsyncIOMotorClient, getenv('DATABASE_URL'))

