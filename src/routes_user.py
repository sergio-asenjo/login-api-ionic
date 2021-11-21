import bcrypt
import os
from fastapi import APIRouter
from src.db import connection
from src.model_user import users
from src.schema_user import User
from sqlalchemy.exc import IntegrityError

user = APIRouter()
PEPPER = os.environ["PEPPER"]

@user.get("/usuario/{id}")
async def read_user(id: int):
    return connection.execute(users.select().where(users.c.id_usuario == id)).fetchall()

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
    except Exception as ex:
        return {}

@user.put("/{id}")
async def update_user(id: int, user: User):
    connection.execute(users.update().values(
        nombre_usuario=user.nombre,
        correo_usuario=user.email,
        contrasena_usuario=user.password
    ).where(users.c.id_usuario == id))
    return connection.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_user(id: int):
    connection.execute(users.delete().where(users.c.id_usuario == id))
    return connection.execute(users.select()).fetchall()