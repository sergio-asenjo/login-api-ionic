from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, CHAR
from src.db import meta

users = Table('Usuario', meta,
                Column('id_usuario', Integer, primary_key=True),
                Column('nombre_usuario', String(50), unique=True),
                Column('contrasena_usuario', CHAR),
                Column('correo_usuario', String(50)))