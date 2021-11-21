from fastapi import APIRouter
from src.db import connection
from src.model_user import users
from src.schema_user import User

user = APIRouter()

@user.get("/usuario/{id}")
async def read_user(id: int):
    return connection.execute(users.select().where(users.c.id_usuario == id)).fetchall()

@user.post("/usuario")
async def write_user(user: User):
    connection.execute(users.insert().values(
        nombre_usuario=user.nombre,
        correo_usuario=user.email,
        contrasena_usuario=user.password
    ))
    return connection.execute(users.select()).fetchall()

@user.post("/login")
async def login_user(user: User):
    try:
        response = connection.execute(users.select().where(
                    users.c.nombre_usuario == user.nombre).where(
                    users.c.contrasena_usuario == user.password)).fetchone()
        return {"id": response[0]}
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