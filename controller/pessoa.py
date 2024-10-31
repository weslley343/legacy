from database.supabase import supabase
from ulid import ULID
from datetime import datetime
from typing import Optional

class Pessoa:
    @staticmethod
    def create_pessoa(nome: str, descricao: Optional[str], nascimento: Optional[datetime], morte: Optional[datetime], image: Optional[str]):
        ulid = str(ULID())  # Gera um ULID único
        data = {
            "ulid": ulid,
            "nome": nome,
            "descricao": descricao,
            "nascimento": nascimento,
            "morte": morte,
            "image": image
        }
        response = supabase.table("pessoas").insert(data).execute()
        return response.data

    @staticmethod
    def get_pessoa(ulid: str):
        response = supabase.table("pessoas").select("*").eq("ulid", ulid).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all_pessoas():
        response = supabase.table("pessoas").select("*").execute()
        return response.data

    @staticmethod
    def update_pessoa(ulid: str, nome: Optional[str], descricao: Optional[str], nascimento: Optional[datetime], morte: Optional[datetime], image: Optional[str]):
        data = {k: v for k, v in locals().items() if v is not None and k != "ulid"}
        response = supabase.table("pessoas").update(data).eq("ulid", ulid).execute()
        return response.data

    @staticmethod
    def delete_pessoa(ulid: str):
        response = supabase.table("pessoas").delete().eq("ulid", ulid).execute()
        return response.data
    
    @staticmethod
    def buscar_pessoas_por_nome(nome_parcial: str):
        response = supabase.table("pessoas").select("*").ilike("nome", f"%{nome_parcial}%").execute()
        return response.data
