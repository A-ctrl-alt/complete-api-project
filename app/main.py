from enum import Enum

from fastapi import Body, FastAPI, HTTPException, status

from app.schemas import ShipCreate


class ShipmentStatus(str, Enum):
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    PENDING = "pending"
    CANCEL = "cancel"



app = FastAPI()

shipments = {
    1270: {"weight": 12.5, "content": "wooden table", "status": "delivered"},
    1271: {"weight": 13.5, "content": "toys", "status": "pending"},
    1272: {"weight": 10.2, "content": "chair", "status": "shipped"},
    1273: {"weight": 5.1, "content": "books", "status": "pending"},
    1274: {"weight": 22.0, "content": "refrigerator", "status": "delivered"},
    1275: {"weight": 3.7, "content": "clothes", "status": "shipped"},
    1276: {"weight": 8.9, "content": "shoes", "status": "pending"},
    1277: {"weight": 15.0, "content": "monitor", "status": "delivered"},
    1278: {"weight": 6.3, "content": "keyboard", "status": "shipped"},
    1279: {"weight": 1.1, "content": "mouse", "status": "pending"},
}


@app.get("/shipments/latest")
def get_latest_shipment():
    latest_id = max(shipments.keys())
    return shipments[latest_id]


@app.get("/shipments/{id}")
def get_shipments_by_id(id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with that id not found",
        )
    return shipments[id]


@app.post("/new_shipments")
def new_shipments(weight: float = Body(...), content: str = Body(...)):
    if weight <= 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="weight must be greater than zero",
        )

    new_id = max(shipments) + 1
    shipments[new_id] = {"weight": weight, "content": content, "status": "pending"}
    return shipments[new_id]


@app.put("/update-shipments")
def update_shipments(id: int, weight: float, content: str):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with that id not found",
        )

    shipments[id].update({"weight": weight, "content": content})
    return {"message": f"shipment with the id {id} updated successfully"}


@app.patch("/update-shipment/{id}")
def update_the_shipments(
    id: int,
    weight: float | None = Body(None),
    content: str | None = Body(None),
):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="shipment with that id not found",
        )

    if weight is not None and weight <= 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="weight must be greater than zero",
        )

    if weight is not None:
        shipments[id]["weight"] = weight
    if content is not None:
        shipments[id]["content"] = content

    return {"message": f"shipment with the id {id} updated successfully"}


@app.delete("/remove-shipments/{id}")
def delete_shipments(id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="shipment with that id not found",
        )

    shipments.pop(id)
    return {"message": f"shipments with the id {id} deleted successfully"}


@app.post("/create-shipments")
def create_shipments(shipment: ShipCreate):
    new_id = max(shipments) + 1
    shipments[new_id] = {
        "weight": shipment.weight,
        "content": shipment.content,
        "status": "placed",
    }
    return shipments[new_id]

@app.post("/create_new_shipment")
def create_new_shipment(shipment: ShipCreate):
    new_id = max(shipments) + 1
    new_content = {
        "weight": shipment.weight,
        "content": shipment.content,
        "status": "placed",
    }
    shipments.update({new_id: new_content})
    return {"message": shipments[new_id]}

@app.put("/update-shipments/{sid}")
def update_shipments_by_id(sid: int, data: ShipCreate):
    if sid not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with that id not found",
        )

    shipments[sid] = {
        "id": sid,
        "weight": data.weight,
        "content": data.content,
        "status": shipments[sid].get("status", "pending"),
    }
    return shipments[sid]





