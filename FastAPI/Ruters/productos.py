from fastapi import APIRouter

# para que el secidor corra o ejecute: python -m uvicorn FastAPI.productos:app --reload
router = APIRouter()

@router.get("/productos")
async def productos():
    return ["Producto 1", "Producto 2", "Producto 3"]