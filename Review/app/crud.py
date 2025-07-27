from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.name == user.name).first()
    if existing_user:
        raise ValueError("Пользователь с таким именем уже существует")

    hashed_password = bcrypt.hash(user.password)
    db_user = models.User(name=user.name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()



def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(content=review.content, user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session):
    return db.query(models.Review).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()
