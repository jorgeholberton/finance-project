""" Schemas for Stock API """

from pydantic import  BaseModel,Field
##pydantic permite definir esquemas, contratos  que dicen que se puede recibir en el cuerpo 
#de una petición
#se debe importar pydantic, en el terminal poetry add pydantic
#los schemas son solo para validar la informacion que llega
#hacen parte de las appis, endpoints

class StockSchema(BaseModel):
    name: str = Field(max_length=20)##Field permiten validar tamaños
    price: int = Field(gt=0) #greater than
    code: str = Field(max_length=7)