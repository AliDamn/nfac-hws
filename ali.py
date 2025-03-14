from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from starlette.requests import Request
import uvicorn

app = FastAPI()


cars = [{"id": i, "name": f"Car {i}", "year": str(2000 + i % 20)} for i in range(1, 101)]
users = [{"id": i, "email": f"user{i}@test.com", "first_name": f"First{i}", "last_name": f"Last{i}", "username": f"user{i}"} for i in range(1, 21)]


templates = Jinja2Templates(directory="templates")

@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    return cars[start:(start + limit)]

@app.get("/cars/{id}")
def get_car(id: int):
    for car in cars:
        if car["id"] == id:
            return car
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users/{id}", response_class=HTMLResponse)
def get_user(request: Request, id: int):
    for user in users:
        if user["id"] == id:
            return templates.TemplateResponse("user.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="Not found")


if __name__=="__main__":
    uvicorn.run(app,port=8006)






