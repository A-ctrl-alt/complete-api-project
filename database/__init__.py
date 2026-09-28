from dataclasses import Field
from datetime import datetime

from sqlmodel import SQLModel
from enum import Enum

class Shipmentsstatus(str, Enum):
    PLACED = "placed"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    in_transit = "in_transit"

class Shipments(SQLModel):
    _tablename_="ships"
    id:int|None= Field(default=None,primary_key=True)
    content:str
    weight:float
    status:str
    destination:str
    expected_delivery:datetime

