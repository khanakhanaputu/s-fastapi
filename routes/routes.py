from fastapi import APIRouter
from database.database import fake_db
from controllers.ItemController import Item

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
async def tambah_menu(item: Item):
    fake_db.update({{"name": item.name, "price": item.price}})
    return fake_db


# @router.put("/ubah/{item_name}")
# async def ubah_menu(item_name: str):
#     for i in fake_db:
#         if fake_db["name"] == item_name:
#             fake_db["name"] = item_name
