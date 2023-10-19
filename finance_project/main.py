""" Main module of finance application """

from typing import List
from fastapi import FastAPI, HTTPException
from finance_project.models.stocks import Stock
from  finance_project.schemas.stock_schemas import StockSchema

app=FastAPI()
#asigna el tipo a la variable 
stocks: List[Stock]=[
    Stock("Apple Company",102,"AAPL.US"),
    Stock("Microsoft Company",78,"MICRO.US"),
    Stock("Google Company",92,"GGLE.US"),
]

@app.get("/stocks")
def get_stocks():
    print(str(stocks))
    return stocks

@app.get("/stocks/{code}")
def get_stocks_id(code: str):
    for item in stocks:
        if code==item.code:
            return item
    raise HTTPException(status_code=404, detail="Code Company doesn't exists")
    #return None 
        
            
            
    

##llamar ruta con post, creando endpoint para llamar objetos
@app.post("/stocks/create-stock")
def create_stocks(stock_body: StockSchema):##StockSchema valida los datos
    stock=Stock(**stock_body.model_dump()) #Kwargs: keyword arguments, model_dump coge el obejto y lo coloca en el diccionario
    stocks.append(stock) 