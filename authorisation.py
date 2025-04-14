from fastapi import FastAPI, Request, Form, Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from repository import UsersRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")

user_repo = UsersRepository()

@app.get("/signup", response_class=HTMLResponse)
def get_signup_form(request: Request):
    return templates.TemplateResponse("authorisation.html", {"request": request})

@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request, email: str = Form(...), password: str = Form(...), full_name: str = Form(...)):
    if email in user_repo.users_db:
        raise HTTPException(status_code=404, detail='Email already registered')

    user_repo.create_user(email, full_name, password)
    return RedirectResponse("/login", status_code=303)

@app.get("/login", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_confirm(request: Request, email: str = Form(...), enter_password: str = Form(...), response: Response = None):
    user = user_repo.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["password"] != enter_password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    response.set_cookie(key="user_email", value=email, httponly=True)

    return RedirectResponse("/profile", status_code=303)

@app.get("/profile",response_class=HTMLResponse)
async def dashboard(request: Request):
    user_email = request.cookies.get("user_email")
    if not user_email:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = user_repo.get_user_by_email(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {}
    for key, value in user.items():
        if key != "password":
            user_data[key] = value

    return templates.TemplateResponse("profile.html",{'request':request, "user":user_data})









