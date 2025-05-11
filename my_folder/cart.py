from fastapi import APIRouter, Request, Form, Response, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from flowers_repository import FlowersRepository
from repository import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart/items")
async def add_to_cart(
    request: Request,
    response: Response,
    flower_id: int = Form(...),
    db: Session = Depends(get_db)
):
    cart = request.cookies.get("cart")
    cart_items = cart.split(",") if cart else []
    cart_items.append(str(flower_id))

    response = RedirectResponse(url="/flowers", status_code=303)
    response.set_cookie(key="cart", value=",".join(cart_items))
    return response

@router.get("/cart/items", response_class=HTMLResponse)
async def show_cart(request: Request, db: Session = Depends(get_db)):
    cart = request.cookies.get("cart")
    cart_items = cart.split(",") if cart else []

    repo = FlowersRepository(db)
    flowers = repo.get_all()
    flowers_by_id = {f.id: f for f in flowers}

    cart_flowers = []
    total_price = 0

    for item in cart_items:
        try:
            flower_id = int(item)
            flower = flowers_by_id.get(flower_id)
            if flower:
                cart_flowers.append({
                    "id": flower.id,
                    "name": flower.name,
                    "price": flower.price_per_item
                })
                total_price += flower.price_per_item
        except ValueError:
            continue

    return templates.TemplateResponse("cart.html", {
        "request": request,
        "cart_items": cart_flowers,
        "total": total_price
    })

