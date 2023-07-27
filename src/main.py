from typing import Union

from fastapi import FastAPI

from src.db.database import Database

from src.router.data import router as data_router

app = FastAPI(
    title="AirHouse API Service",
    version='0.0.1',
)

app.include_router(data_router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}


if __name__ == "__main__":
    Database.init_db()
