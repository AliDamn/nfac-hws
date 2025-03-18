from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi.requests import Request

app = FastAPI()

# База данных
cars = [
    {'id': 1, 'name': 'Ford Model T'},
    {'id': 2, 'name': 'Chevrolet Bel Air'},
    {'id': 3, 'name': 'Cadillac Eldorado'},
    {'id': 4, 'name': 'Buick Roadmaster'},
    {'id': 5, 'name': 'Plymouth Fury'},

    {'id': 6, 'name': 'Ford Fairlane'},
    {'id': 7, 'name': 'Chevrolet Impala'},
    {'id': 8, 'name': 'Cadillac DeVille'},
    {'id': 9, 'name': 'Buick Skylark'},
    {'id': 10, 'name': 'Plymouth Barracuda'},

    {'id': 11, 'name': 'Ford Thunderbird'},
    {'id': 12, 'name': 'Chevrolet Nova'},
    {'id': 13, 'name': 'Cadillac Fleetwood'},
    {'id': 14, 'name': 'Buick Century'},
    {'id': 15, 'name': 'Plymouth Valiant'},

    {'id': 16, 'name': 'Ford Galaxie'},
    {'id': 17, 'name': 'Chevrolet Camaro'},
    {'id': 18, 'name': 'Cadillac Seville'},
    {'id': 19, 'name': 'Buick Riviera'},
    {'id': 20, 'name': 'Plymouth Satellite'}
]

templates = Jinja2Templates(directory='templates')


@app.get("/cars")
def get_cars():
    return cars


@app.get("/cars/search")
def search_cars(request: Request, q: str = ""):
    filtered_cars = []
    for car in cars:
        if q.lower() in car['name'].lower():
            filtered_cars.append(car)

    return templates.TemplateResponse(
        'search.html',
        {'request': request, 'cars': filtered_cars, 'q': q}
    )

class NewCars(BaseModel):
    model: str
@app.get("/cars/new")
async def new_car_form(request: Request):
    return templates.TemplateResponse("new_car.html", {"request": request})


@app.post("/cars/new")
async def add_cars(model: str = Form(...)):
    cars.append({"id": len(cars) + 1, "model": model})
    return RedirectResponse(url="/cars", status_code=303)


@app.get("/cars")
async def get_cars():
    return {"cars": cars}