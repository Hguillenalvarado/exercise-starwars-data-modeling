import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    personaje_id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    Estatura=Column(Integer)
    nacimiento=Column(Integer)

class Planetas(Base):
    __tablename__ = 'Planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planeta_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    poblacion = Column(Integer)
    
class Usuarios(Base):
    __tablename__ = 'Usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    usuario_id = Column(Integer, primary_key=True)
    usuario_name = Column(String(30))
    correo = Column(String(50))
    clave = Column(String(10))
    
class Favoritos(Base):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer,ForeignKey('Usuarios.usuario_id'))
    personaje_id= Column(Integer,ForeignKey('personajes.personaje_id'))
    planeta_id= Column(Integer,ForeignKey('Planetas.planeta_id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')