from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return "Hola, ¿Que pais te gustaria visitar algun dia?"

@app.get("/paises/{num}")
def pais(num):
    pais={
    "1":"Alemania",
    "2":"España",
    "3":"Portugal",
    "4":"Ucrania"

    }
    return pais

@app.get("/Conversor_CaF/{C}")
def conversorCaf(C):
       try: 
                C=float(C)
                TF=C*(9/5) + 32
                return f"La temperatura es de {TF} grados farenheit"
       except: 
                return "Entrada invalida"
