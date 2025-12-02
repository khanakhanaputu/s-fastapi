from fastapi import APIRouter

router = APIRouter()


# create a router here :)
@router.get("/")
async def home():
    return {"message": "Lmao"}


@router.get("/blog/{id}/{comment}")
async def blog(id: int, comment: str):
    return {"data": {"id": id, "comment": comment}}
