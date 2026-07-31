from fastapi import FastAPI,HTTPException  
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

@app.get("/user/{id}", response_model=User)
async def user(id: int):
    return search_user(id)

@app.get("/user/", response_model=User)
async def user(id: int):
    return search_user(id)

@app.post("/user/", response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=304, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user

@app.put("/user/", response_model=User)
async def user(user: User):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    
    if not found:
        raise HTTPException(status_code=304, detail="El usuario no existe")

@app.delete("/user/{id}",response_model=User)
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            raise HTTPException(status_code=204, detail="El usuario ha sido eliminado")
    
    if not found:
        raise HTTPException(status_code=404, detail="El usuario no existe")

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "El usuario no existe"}