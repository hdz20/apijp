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

@app.get("/Conversor_Caf/{K}")
def conversorCaf(K):
     try:
            k=float(k)
            TF=k*(K-273) + 32
            return k"la temperatura es de {TF} grados Fahrenheit"
     except:
            return "Entrada Invalida"
