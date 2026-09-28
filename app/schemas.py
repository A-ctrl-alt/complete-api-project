from pydantic import BaseModel


class ShipBase(BaseModel):
    weight: float
    content: str


class ShipCreate(ShipBase):
    pass


class Ship(ShipBase):
    id: int
    status: str = "pending"
