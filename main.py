from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
	return "Hola preciosa, tas bimbonita"
