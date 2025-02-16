from conexion import ModeloBase

from sqlalchemy import Column,ForeignKey, Integer,String


class Departamento(ModeloBase):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True )
    nombre = Column(String, nullable=False, unique=True)

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Empleado(ModeloBase):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True)
    nombre = Column(String,nullable=False)
    apeliido = Column(String, nullable=False)
    documento = Column(String, nullable=False, unique=True)
    id_departamento = Column(Integer, ForeignKey("departamento.id"))

    def __init__(self, nombre,apellido, documemto, id_departamento):
        self.nombre = nombre
        self.apeliido = apellido
        self. documento = documemto
        self.id_departamento = id_departamento

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apeliido} "