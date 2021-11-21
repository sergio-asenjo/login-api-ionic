import bcrypt
import os
from fastapi import APIRouter
from src.db import connection
from src.model_user import users
from src.schema_user import User
from sqlalchemy.exc import IntegrityError

user = APIRouter()
PEPPER = os.environ["PEPPER"]

@user.get("/usuario/")
async def read_user(usuario: str, correo: str):
    try:
        exists = connection.execute(users.select().where(
                        users.c.nombre_usuario == usuario)
                        .where(users.c.correo_usuario == correo)).fetchone()
        if exists:
            return {"id": exists[0]}
        return {"usuario": "no existe"}
    except:
        return {"usuario": "no existe"}

@user.post("/registro")
async def write_user(user: User):
    try:
        hashed_pwd = bcrypt.hashpw((user.password + PEPPER).encode('utf-8'), bcrypt.gensalt())
        connection.execute(users.insert().values(
            nombre_usuario=user.nombre,
            correo_usuario=user.email,
            contrasena_usuario=hashed_pwd
        ))
        return {'registro': '¡Registro exitoso!'}
    except IntegrityError:
        return {'registro': '¡Correo ya existe!'}


@user.post("/login")
async def login_user(user: User):
    try:
        response = connection.execute(users.select().where(
                    users.c.nombre_usuario == user.nombre)).fetchone()
        if bcrypt.checkpw((user.password + PEPPER).encode('utf-8'), response[2].encode('utf-8')):
            return {"id": response[0]}
        else:
            return {}
    except:
        return {}

@user.patch("/recuperar")
async def update_pwd_user(user: User):
    try:
        exists = connection.execute(users.select().where(users.c.nombre_usuario == user.nombre)
        .where(users.c.correo_usuario == user.email)).fetchone()
        if exists:
            hashed_pwd = bcrypt.hashpw((user.password + PEPPER).encode('utf-8'), bcrypt.gensalt())
            connection.execute(users.update().values(
                contrasena_usuario=hashed_pwd
            ).where(users.c.nombre_usuario == user.nombre)
            .where(users.c.correo_usuario == user.email))
            return {'recuperacion': 'exitosa'}
        else: return {'recuperacion': 'fallida'}
    except:
        return {'recuperacion': 'fallida'}

@user.put("/actualizar/{id}")
async def update_user(id: int, user: User):
    try:
        exists = connection.execute(users.select().where(users.c.id_usuario == id)).fetchone()
        if exists:
            hashed_pwd = bcrypt.hashpw((user.password + PEPPER).encode('utf-8'), bcrypt.gensalt())
            connection.execute(users.update().values(
                nombre_usuario=user.nombre,
                contrasena_usuario=hashed_pwd,
                correo_usuario=user.email
            ).where(users.c.id_usuario == id))
            return {'actualizacion': 'exitosa'}
        else: return {'actualizacion': 'fallida'}
    except:
        return {'actualizacion': 'fallida'}

@user.delete("/borrar/{id}")
async def delete_user(id: int):
    try:
        exists = connection.execute(users.select().where(users.c.id_usuario == id)).fetchone()
        if exists:
            connection.execute(users.delete().where(users.c.id_usuario == id))
            return {"eliminacion": "exitosa"}
        else: return {"eliminacion": "fallida"}
    except:
        return {"eliminacion": "fallida"}