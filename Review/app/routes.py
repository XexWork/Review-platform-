from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from .database import get_db
from . import crud, schemas
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def pereadres():
    return RedirectResponse(url="/login")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/reviews", response_class=HTMLResponse)
async def reviews_page(request: Request, db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db)
    return templates.TemplateResponse("reviews.html", {"request": request, "reviews": reviews})

@router.get("/products", response_class=HTMLResponse)
async def products_page(request: Request, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

@router.post("/register")
async def register_user(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    if not (3 <= len(username) <= 20):
        raise HTTPException(status_code=400, detail="Имя пользователя 3–20 символов")
    if not (6 <= len(password) <= 50):
        raise HTTPException(status_code=400, detail="Пароль 6–50 символов")

    try:
        crud.create_user(db, schemas.UserCreate(username=username, password=password))
    except ValueError:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    return RedirectResponse(url="/login", status_code=303)

@router.post("/login")
async def login_user(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_username(db, username)
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    return RedirectResponse(url="/reviews", status_code=303)
