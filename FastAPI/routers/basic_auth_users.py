# Inicio del servidor: python -m uvicorn routers.basic_auth_users:router --reload
from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


#APIrouter app instance
router = APIRouter()
# Autenticacion por oauth2
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
# es un formato para mostrar datos de los usuarios
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# es un formato para mostrar datos de los usuarios en la base de datos
class UserInDB(User):
    password: str

#base de datos de usuarios (simulada)
users_db = {
    "maoredev": {
        "username": "maoredev",
        "full_name": "Cristian Gonzalez",
        "email": "montolla@gmail",
        "disabled": False,
        "password": "123456"
    },
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "polo@gmail.com",
        "disabled": True,
        "password": "654321"}      
}

#Esta funcion es para buscar un usuario en la base de datos simulada y devolverlo como un objeto UserInDB
def search_user_db(username: str):
    if username in users_db:
        return UserInDB(**users_db[username])
    
#Esta funcion es para buscar un usuario en la base de datos simulada y devolverlo como un objeto User
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

#Esta funcion es para obtener el token del usuario y verificar si es valido, si no lo es, devuelve un error 401
async def current_token(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="Credenciales de autenticación inválidas",
                               headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Usuario inactivo")
    return user

#Esta funcion es para iniciar sesion con el usuario y la contraseña, si son correctos, devuelve un token de acceso (siendo el token como una llave de acceso)
@router.post("/login/basic")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
    user = search_user_db(form.username)

    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")
    
    return {"access_token": user.username, "token_type": "bearer"}

#Esta funcion es para obtener los datos del usuario que ha iniciado sesion, usando el token de acceso
@router.get("/users/me/basic")
async def me(user: User = Depends(current_token)):
    return user