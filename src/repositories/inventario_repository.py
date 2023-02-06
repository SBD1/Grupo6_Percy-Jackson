from typing import Optional

from database.database_handler import DatabaseHandler
from model.inventario import Inventario


class InventarioRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler()

    def updateInvetario(self, user: Inventario) -> None:
        assert user.id is not None
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "UPDATE INTO public.Inventario(tamanho_inventario, momento_coleta_Item, id_item, id_jogador) VALUES(%s, %s, %s, %s)",
                    [user.tamanho_inventario, user.momento_coleta_Item, user.id_item, user.id_jogador]  
                 )
    
    def deleteUser(self, id) -> None:
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.Jogador WHERE id = %s",
                    [id]
                )
    
    def findInventaryByUserId(self, userId) -> Optional[Inventario]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                   """SELECT * FROM public.Inventario 
                   join Item on Item.id = Inventario.id_item
                   WHERE id_jogador = %s
                   """,
                    [userId]
                )
                result = cursor.fetchone()
    
        if result is None:
            print(f'Inventario com id {id} não encontrado!')
            return None
        
        print(result)
        user = Inventario(*result)
        
        return user
    
    def findAll(self) -> list[Inventario]: 
        with self.db.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                     "SELECT tamanho_inventario, momento_coleta_Item, id_item, id_jogador, id FROM public.Inventario WHERE id = %s",
                      )
                result = cursor.fetchall()
        
        users = [Inventario(*row) for row in result]
        
        return users    