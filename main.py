from fastapi import FastAPI
from fastapi import Body
from fastapi import status

from typing import Annotated

app = FastAPI()
"""
@app.post("/items", response_model=dict[str, str], status_code = HTTPStatus.CREATED.value)
async def create_item(name: Annotated[str, Body(embed = True)]) -> dict:
  return {"name": name}
"""

# Shortcut to remember the names
@app.post("/items", response_model = dict[str, str], status_code = status.HTTP_201_CREATED)
async def create_item(name: Annotated[str, Body(embed = True)]) -> dict:
  return {"name": name}
