import uvicorn

from fastapi import FastAPI

from app import models
from app.database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)