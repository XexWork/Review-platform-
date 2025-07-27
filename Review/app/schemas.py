from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    name: constr(min_length=3, max_length=20)
    password: constr(min_length=6, max_length=50)

class UserOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


class ReviewCreate(BaseModel):
    content: constr(min_length=1, max_length=500)

class ReviewOut(BaseModel):
    id: int
    content: str
    user_id: int
    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: constr(min_length=1, max_length=500)

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        orm_mode = True
