from fastapi import FastAPI, Request, Form, Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from repository import UsersRepository
from fastapi.security import  OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_repo = UsersRepository()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.get("/signup", response_class=HTMLResponse)
def get_signup_form(request: Request):
    return templates.TemplateResponse("authorisation.html", {"request": request})

@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request, email: str = Form(...), password: str = Form(...), full_name: str = Form(...)):
    if email in user_repo.users_db:
        raise HTTPException(status_code=404, detail='Email already registered')
    user_repo.create_user(email, full_name, password)
    return JSONResponse("Ok",status_code=200)

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

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": email}, expires_delta=access_token_expires)

    response = RedirectResponse(url="/profile", status_code=303)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response

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









