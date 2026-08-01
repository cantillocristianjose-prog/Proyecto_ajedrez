#iniciar el servidor: python -m uvicorn routers.jwt_auth_users:router --reload
# deacargar: pip install python-jose[cryptography] y pip install "passlib[bcrypt]"
from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

#Metodo de encriptacion
ALGORITHM = "HS256"
#Token de acceso
ACCESS_TOKEN_DURATION = 1

SECRET = "akaskaldjhgfhjh8721647948394i5iynmdnj"
#APIRouter app instance
router = APIRouter()
#contexto de encriptacion
crypt = CryptContext(schemes=["bcrypt"])

# Autenticacion por jwt
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
        "password": "$2a$12$bbPdiFs3TIDqHA52TjG8lucLmlZsujgSCABHTFtIfRegDlEH0N/Yu"
    },
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "polo@gmail.com",
        "disabled": True,
        "password": "$2a$12$JwVAuwxOuYXfqu0lfi07Q.L/HU1J.MZQoUuSX8he.gehqhepUtjxW"}      
}
#Esta funcion es para buscar un usuario en la base de datos simulada y devolverlo como un objeto UserInDB
def search_user_db(username: str):
    if username in users_db:
        return UserInDB(**users_db[username])

#Esta funcion es para buscar un usuario en la base de datos simulada y devolverlo como un objeto User
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

#autenticacion del usuario con jwt
async def auth_user(token: str = Depends(oauth2)):

        exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail="Credenciales de autenticación inválidas",
                                headers={"WWW-Authenticate": "Bearer"})

        try:
            username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
            if username is None:
                raise exeption

        except JWTError:
            raise exeption

        return search_user(username)

            


#Esta funcion es para obtener el token del usuario y verificar si es valido, si no lo es, devuelve un error 401
async def current_token(user: User= Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Usuario inactivo")
    return user

@router.post("/login/jwt")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")

 

    access_token = {"sub": user.username, 
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION) }

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

#Esta funcion es para obtener los datos del usuario que ha iniciado sesion, usando el token de acceso
@router.get("/users/me/jwt")
async def me(user: User = Depends(current_token)):
    return user