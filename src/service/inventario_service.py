from typing import Optional

from model.inventario import Inventario
from repositories.inventario_repository import InventarioRepository


class InventarioService:
    def __init__(self):
        self.inventarioRepository = InventarioRepository()
    
    def openInventary(self, userId):
        salaAtual = self.inventarioRepository.findInventaryByUserId(userId)

        if(salaAtual is None):
            print("Inventario está vazio!")

            print('Aperte qualquer tecla para continuar: \n')

            inp = input('> ')

            return None

        return salaAtual
    
