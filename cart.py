from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from flowers_repository import UsersRepository

app = FastAPI()
templates = Jinja2Templates(directory="templates")
flower_repo = UsersRepository()

@app.post("/cart/items")
async def add_to_cart(request: Request, response: Response, flower_id: int = Form(...)):
    cart = request.cookies.get("cart")
    if cart:
        cart_items = cart.split(",")
    else:
        cart_items = []

    cart_items.append(str(flower_id))
    response = RedirectResponse(url="/flowers", status_code=303)
    response.set_cookie(key="cart", value=",".join(cart_items))
    return response

@app.get("/cart/items", response_class=HTMLResponse)
async def show_cart(request: Request):
    cart = request.cookies.get("cart")
    cart_items = cart.split(",") if cart else []

    flowers = list(flower_repo.flowers_db.items())
    cart_flowers = []
    total_price = 0

    for item in cart_items:
        try:
            idx = int(item)
            if 0 <= idx < len(flowers):
                name, (price, _) = flowers[idx]
                cart_flowers.append({"id": idx, "name": name, "price": price})
                total_price += price
        except ValueError:
            continue

    return templates.TemplateResponse("cart.html", {
        "request": request,
        "cart_items": cart_flowers,
        "total": total_price
    })
