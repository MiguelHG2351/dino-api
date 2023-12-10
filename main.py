from fastapi import FastAPI

app = FastAPI()

BASE_API = '/api/v1'

@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI"}


@app.get('/api/tasks')
async def get_tasks():
    return 'All tasks'
