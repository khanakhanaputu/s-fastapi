from fastapi import APIRouter
from database.database import fake_db
from 

router = APIRouter()


# create a router here :)
@router.get("/")
async def home():
    return {"message": "Lmao"}


@router.get("/blog/{id}/{comment}")
async def blog(id: int, comment: str):
    return {"data": {"id": id, "comment": comment}}


@router.get("/item")
def get_item():
    return fake_db

@router.post("/tambah")
async def tambah_menu():
    pass
