from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return"Hola a todos, ¿Que marca de carro de gustaria tener?"

@app.get("/")
def index():
    return "hola a todos "
@app.get("/carros/{num}")
def carros(num):
    carros={
     1"Audi"
     2"BMW"
     3"Mercedes Benz"
     4"Porsche"
    }
    return carros

@app.get("/conversor_caf/{C}")
def temp{C}:
     try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"la temperatura es de {TF} grados sentigrados"
    except:
            return"eso no era"
