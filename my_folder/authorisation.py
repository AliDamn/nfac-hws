from fastapi import Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from repository import UsersRepository
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from repository import SessionLocal
from fastapi import APIRouter

router = APIRouter()
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# signup
@router.get("/signup", response_class=HTMLResponse)
def get_signup_form(request: Request):
    return templates.TemplateResponse("authorisation.html", {"request": request})

@router.post("/signup", response_class=HTMLResponse)
async def signup(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(...),
    db: Session = Depends(get_db)
):
    user_repo = UsersRepository(db)

    if user_repo.get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Email already registered")

    user_repo.create_user(email, full_name, password)
    return JSONResponse(content={"message": "Ok"}, status_code=200)

# login
@router.get("/login", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_confirm(
    request: Request,
    email: str = Form(...),
    enter_password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_repo = UsersRepository(db)
    user = user_repo.get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != enter_password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": email}, expires_delta=access_token_expires)

    response = RedirectResponse(url="/profile", status_code=303)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    response.set_cookie(key="user_email", value=email)
    return response

@router.get("/profile", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user_email = request.cookies.get("user_email")
    if not user_email:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_repo = UsersRepository(db)
    user = user_repo.get_user_by_email(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {
        "email": user.email,
        "full_name": user.full_name,
    }

    return templates.TemplateResponse("profile.html", {'request': request, "user": user_data})








