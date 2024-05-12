from fastapi import FastAPI
from fastapi import Body
from trading_ig import rest
from trading_ig_config import config

app = FastAPI()
service = rest.IGService(
    api_key= config.api_key,
    username= config.username,
    password= config.password
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fetch-open-position")
async def fetch_open_position():
    print(Body())
    return Body()

@app.get("/fetch/accounts")
async def fetch_accounts():
    result = service.fetch_accounts()
    return result

