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
    
    def updateSala(self, user: User, opcao: int) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "UPDATE INTO public.Jogador(nome, vida, progresso, ataque, defesa, id_sala, id_nivel) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                    [user.id_sala]  
                 )
