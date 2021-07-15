import uvicorn

from typing import Optional

from fastapi import FastAPI

from .import schemas

app = FastAPI()


@app.delete('/')
async def delete_whole_data():
    return {"data"}

@app.post('/bot-init')
async def initialize_bots():
    return {"data"}

@app.post('/call-start')
async def call_start():
    return {"data"}

@app.post('/call-stop')
async def user_text():
    return {"data"}

@app.post('/bot-user-text')
async def user_text():
    return {"data"}

@app.post('/bot-text')
async def bot_text():
    return {"data"}

@app.get('/customers')
async def read_customers():
    return {"data"}

@app.get('/customers/{phone_number}')
async def dialogues():
    return {"data"}

@app.post('/customers/')
async def dialogues():
    return {"data"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)