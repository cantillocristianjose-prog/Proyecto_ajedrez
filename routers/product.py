from fastapi import APIRouter

router = APIRouter(prefix = "/productos", tags = ["productos"],responses = {404: {"message": "No encontrado"}})

productos_lista = ["Producto 1", "Producto 2", "Producto 3"]

@router.get("/")
async def productos():
    return productos_lista

@router.get("/{id}")
async def producto(id: int):
    try:
        return productos_lista[id]
    except:
        return {"error": "No se ha encontrado el producto"}
