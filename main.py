from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return "Hola, ¿Que marca de carro de gustaria tener algun dia?"

@app.get("/naves/{num}")
def carro(num):
    carros={
    "1 Audi",
    "2 BMW",
    "3 Mercedes Benz",
    "4 Porsche"

    }
    return num

@app.get("/Conversor_CaF/{C}")
def conversorCaf(C):
       try: 
                C=float(C)
                TF=C*(9/5) + 32
                return f"La temperatura es de {TF} grados farenheit"
       except: 
                return "Entrada invalida"
