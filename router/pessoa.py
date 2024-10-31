from fastapi import APIRouter, HTTPException
from controller.pessoa import Pessoa
from datetime import date
from typing import Optional, List

pessoa_router = APIRouter()

@pessoa_router.post("/pessoas/")
async def create_pessoa(nome: str, descricao: Optional[str] = None, nascimento: Optional[date] = None, morte: Optional[date] = None, image: Optional[str] = None):
    try:
        pessoa = Pessoa.create_pessoa(nome, descricao, nascimento, morte, image)
        if not pessoa:
            raise HTTPException(status_code=400, detail="Erro ao criar pessoa")
        return pessoa
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@pessoa_router.get("/pessoas/{ulid}")
async def get_pessoa(ulid: str):
    pessoa = Pessoa.get_pessoa(ulid)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa

@pessoa_router.get("/pessoas/")
async def get_all_pessoas():
    return Pessoa.get_all_pessoas()

@pessoa_router.put("/pessoas/{ulid}")
async def update_pessoa(ulid: str, nome: Optional[str] = None, descricao: Optional[str] = None, nascimento: Optional[date] = None, morte: Optional[date] = None, image: Optional[str] = None):
    pessoa = Pessoa.update_pessoa(ulid, nome, descricao, nascimento, morte, image)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Erro ao atualizar pessoa")
    return pessoa

@pessoa_router.get('/pessoas/byname/{name}')
async def get_pessoa_by_name(name: str):
    pessoas = Pessoa.buscar_pessoas_por_nome(name)
    if not pessoas:
        raise HTTPException(status_code=404, detail="Nenhuma pessoa encontrada com esse nome")
    return pessoas

@pessoa_router.delete("/pessoas/{ulid}")
async def delete_pessoa(ulid: str):
    pessoa = Pessoa.delete_pessoa(ulid)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {"detail": "Pessoa excluída com sucesso"}
