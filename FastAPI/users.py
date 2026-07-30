from fastapi import FastAPI
app = FastAPI()

# Iniciar el servidor:  cd FastAPI python -m uvicorn users:app --reload
@app.get("/users")
async def users():
    return "¡hola api!"