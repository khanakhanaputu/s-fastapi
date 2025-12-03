from pydantic import BaseModel


class Menu(BaseModel):
    nama: str
    harga: int
