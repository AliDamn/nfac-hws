from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from flowers_repository import UsersRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")

flowers_db = {}

flower = UsersRepository()

class Flowers(BaseModel):
    name: str
    quantity: int
    price_per_item: int

@app.get("/flowers", response_class=HTMLResponse)
async def add_flowers(request: Request):
    return templates.TemplateResponse("flowers.html", {"request": request, "flowers": flower.flowers_db})

@app.post("/flowers", response_class=HTMLResponse)
async def get_flowers(request: Request, price_per_item: int, name: str, quantity: int):
    flower.create_item(price_per_item, quantity, name)
    return RedirectResponse("/flowers",status_code=303)





