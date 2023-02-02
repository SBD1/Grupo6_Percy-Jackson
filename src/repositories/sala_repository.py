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
                     "UPDATE public.Jogador SET id_sala = %s WHERE id = %s ",
                    [opcao, user.id]  
                 )
    
    def findSalaById(self, id) -> Optional[Sala]:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, descricao, id_nivel, destinos FROM public.Sala WHERE id = %s",
                    [id]
                )
                result = cursor.fetchone()
        
        if result is None:
            print(f'Sala com id {id} não encontrada!')
            return None
        
        sala = Sala(*result)
        
        return sala

    def encontrarInimigos(self, user: User):
       # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                        FROM public.comum
                        join public.inimigo on public.comum.id_inimigo = public.inimigo.id
                        join public.npc on public.npc.id_sala = %s and public.inimigo.id_npc=npc.id;
                    """,
                        [user.id_sala])
                inimigos = cursor.fetchone()
        
        return inimigos
    
    def encontrarBoss(self, user: User):
       
       # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * 
                        from boss
                        join inimigo on boss.id_inimigo = inimigo.id
                        join npc on npc.id_sala = %s and inimigo.id_npc=npc.id
                    """,
                        [user.id_sala])
                boss = cursor.fetchone()
        
        return boss
    
    def encontrarBau(self, user: User):
        # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                        FROM public.Bau WHERE id_sala = %s
                    """,
                        [user.id_sala])
                bau = cursor.fetchone()
        
        return bau
    
    def abrirBau(self, user: User):
        # print(user) 
        
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                        FROM public.Bau
                        JOIN public.Item ON public.Bau.id_item = public.Item.id
                        WHERE id_sala = %s
                    """,
                        [user.id_sala])
                item = cursor.fetchone()
        
        return item