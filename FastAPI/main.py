from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return "¡hola api!"

@app.get("/url")
async def url():
    return {"url": "https://www.example.com"}

# Iniciar el servidor:  python -m uvicorn FastAPI.main:app --reload
# Detenerlo con Ctrl + C

# documentacion http://127.0.0.1:8000/docs o http://127.0.0.1:8000/redoc
