from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .routes import montadora, modelo, veiculo
from .database import get_db_connection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='app/templates')

app.include_router(montadora.router, prefix="/montadora")
app.include_router(modelo.router, prefix="/modelo")
app.include_router(veiculo.router, prefix='/veiculo')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test_db_connection")#verificar conexão com o banco
def test_db_connection():
    try:
        connection = get_db_connection()
        return {"status": "success", "message": "Database connection established!"}
    except Exception as e:
        return {"status": "failure", "message": f"Error: {str(e)}"}

