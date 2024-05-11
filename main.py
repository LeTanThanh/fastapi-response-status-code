from fastapi import FastAPI
from fastapi import Body

from typing import Annotated

from http import HTTPStatus

app = FastAPI()

@app.post("/items", response_model=dict[str, str], status_code = HTTPStatus.CREATED.value)
async def create_item(name: Annotated[str, Body(embed = True)]) -> dict:
  return {"name": name}
