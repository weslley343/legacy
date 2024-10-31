from fastapi import FastAPI
from router.pessoa import pessoa_router  # Importa o router do arquivo router/pessoa.py

app = FastAPI()

# Inclui as rotas
app.include_router(pessoa_router, prefix="/api", tags=["pessoas"])

@app.get("/")
async def root():
    return {"message": "API de Pessoas com FastAPI e Supabase"}
