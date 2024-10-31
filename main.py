from fastapi import FastAPI
from router.pessoa import pessoa_router  # Importa o router do arquivo router/pessoa.py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Inclui as rotas
app.include_router(pessoa_router, prefix="/api", tags=["pessoas"])

@app.get("/")
async def root():
    return {"message": "API de Pessoas com FastAPI e Supabase"}
