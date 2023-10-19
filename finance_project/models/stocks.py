""" class for stocks model """

from dataclasses import dataclass
#los modelos son los template de los cuales se crean los objetos
#y se conectan a la base de datos, es lo que se quiere representar de la BD

@dataclass
class Stock():
    name: str
    price: int
    code: str
    