from typing import Optional

from model.salas import Sala
from repositories.sala_repository import SalaRepository

from model.users import User

from model.users import User

class SalaService:
    def __init__(self):
        self.salaRepository = SalaRepository()
    
    def mover(self, user: User) -> Optional[Sala]:
        
        salaAtual = self.salaRepository.salaAtual(user)
        
        inp = input("Você possui as seguintes opções:\n" +
                "D - Direita: Sala " + str(salaAtual.destinos[0]) + "\n" +
                "E - Esquerda: Sala " + str(salaAtual.destinos[1]) + "\n" +
                "F - Frente: Sala " + str(salaAtual.destinos[2]) + "\n" +
                "A - Atrás: Sala " + str(salaAtual.destinos[3]) + "\n")
        



        

        return salaAtual.destinos

