#Fast API es un framework web moderno y rápido para construir APIs con Python 3.6+ basado en las anotaciones de tipo estándar de Python.
from fastapi import FastAPI
#importar los routers
from routers import product,users
#importar recursos estaticos
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers la conexion de scrpipts de rutas a la app principal
app.include_router(product.router)
app.include_router(users.router)
#Recursos estaticos (imagenes, css, js)
app.mount("/static"#aqui se pone la ruta en el que se va a ver los recursos estaticos
          , StaticFiles(directory="static") # aqui se define el diccionario
          , name="static") # el nombre que se va a dar

@app.get("/")
async def root():
    return "¡hola api!"

@app.get("/url")
async def url():
    return {"url": "https://www.example.com"}

# Iniciar el servidor:  python -m uvicorn FastAPI.main:app --reload
# Detenerlo con Ctrl + C

# documentacion http://127.0.0.1:8000/docs o http://127.0.0.1:8000/redoc
