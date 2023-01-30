from typing import Optional

from model.salas import Sala
from repositories.sala_repository import SalaRepository

from model.users import User

from model.users import User

class SalaService:
    def __init__(self):
        self.salaRepository = SalaRepository()
    
    def mover(self, user: User) -> Optional[Sala]:
        inp = input("Você possui as seguintes opções:\n" +
                "Direita - D\n" +
                "Esquerda - E\n" +
                "Frente - F\n" +
                "Atrás - A\n")
        
        salaAtual = self.salaRepository.salaAtual(user)

        

        return salaAtual.destinos

