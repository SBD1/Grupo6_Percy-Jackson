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
                    "SELECT id, nome, descricao, id_nivel, destinos FROM public.Sala WHERE id = %s",
                    [user.id_sala]
                        )
                result = cursor.fetchone()

        print(result)
        salaAtual = Sala(*result)
            
        return salaAtual
    
    ''' def findDestinos(self, id_sala) -> list[Sala]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT destinos FROM public.Sala WHERE id = %s",
                    [id_sala]
                        )
                result = cursor.fetchall()
            
       # result1 = Sala(*row) for row in result

        print(result)
            
        return result[0][0] '''
