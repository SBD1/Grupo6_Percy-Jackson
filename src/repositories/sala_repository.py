from typing import Optional

from database.database_handler import DatabaseHandler
from model.salas import Sala

from model.users import User

class SalaRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()
        
    def salaAtual(self, user: User):
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_sala FROM public.Jogador WHERE id = %s",
                    [user.id]
                        )
                result = cursor.fetchall()
            
        return result[0][0]
    
    def findDestinos(self, id_sala) -> list[Sala]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT destinos FROM public.Sala WHERE id = %s",
                    [id_sala]
                        )
                result = cursor.fetchall()
            
       # result1 = Sala(*row) for row in result

        sala = Sala(result)
            
        return sala.destinos
