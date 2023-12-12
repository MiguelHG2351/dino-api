from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from core.fastapi.event.middleware import EventHandlerMiddleware

from database import get_all_dinos
from container import Container

app = FastAPI()

BASE_API = '/api/v1'

container = Container()
# container.wire()

app.container = container
db = container.db

app.add_middleware(EventHandlerMiddleware)

@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI"}


@app.get('/api/tasks')
async def get_tasks():
    dinos = await get_all_dinos()
    return dinos

