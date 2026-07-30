from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#Entidad de usuario (modelo)
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

users_list = [User(id=1, name="Cristian", surname="Gonzalez", email="cristian@example.com", age=25),
              User(id=2, name="Juan", surname="Perez", email="juan@example.com", age=34),
              User(id=3, name="María", surname="López", email="maria@example.com", age=28)]

# Iniciar el servidor:  python -m uvicorn FastAPI.users:app --reload

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@app.get("/user/")
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return {"message": "Usuario creado correctamente"}

@app.put("/user/")
async def user(user: User):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    
    if not found:
        return {"error": "El usuario no existe"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}