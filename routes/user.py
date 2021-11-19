from fastapi import APIRouter
from config.db import connection
from models.index import users
from schemas.index import User

user = APIRouter()

# @user.get("/")
# async def read_users():
#     return connection.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_user(id: int):
    return connection.execute(users.select().where(users.c.id_usuario == id)).fetchall()

@user.post("/")
async def write_user(user: User):
    connection.execute(users.insert().values(
        nombre_usuario=user.nombre,
        correo_usuario=user.email,
        contrasena_usuario=user.password
    ))
    return connection.execute(users.select()).fetchall()

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