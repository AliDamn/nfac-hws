from fastapi import Request, Depends, Form, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from flowers_repository import FlowersRepository
from repository import SessionLocal
from fastapi import APIRouter


router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Flowers(BaseModel):
    name: str
    quantity: int
    price_per_item: int

@router.get("/flowers", response_class=HTMLResponse)
def show_flowers(request: Request, db: Session = Depends(get_db)):
    repo = FlowersRepository(db)
    items = repo.get_all()
    return templates.TemplateResponse("flowers.html", {"request": request, "flowers": items})

@router.post("/flowers", response_class=HTMLResponse)
def get_flowers(request: Request, price_per_item: int = Form(...), name: str = Form(...), quantity: int = Form(...), db: Session = Depends(get_db)):
    repo = FlowersRepository(db)
    repo.create_item(name, quantity, price_per_item)
    return RedirectResponse("/flowers", status_code=303)

@router.patch("/flowers/{flower_id}")
def update_flower(flower_id: int, quantity: int = None, price_per_item: int = None, db: Session = Depends(get_db)):
    repo = FlowersRepository(db)
    updated = repo.update_item(flower_id, quantity, price_per_item)
    if not updated:
        raise HTTPException(status_code=404, detail="Flower not found")
    return {"message": "Flower updated"}

@router.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    repo = FlowersRepository(db)
    deleted = repo.delete_item(flower_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Flower not found")
    return {"message": "Flower deleted"}






