from fastapi import FastAPI
from authorisation import router as auth_router
from flowers import router as flowers_router
from cart import router as cart_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(flowers_router)
app.include_router(cart_router)
