from fastapi import FastAPI
from fastapi import Body
from trading_ig import rest

app = FastAPI()


@app.get("/fetch-open-position")
async def fetch_open_position():
    print(Body())
