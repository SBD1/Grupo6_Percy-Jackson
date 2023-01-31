from typing import Optional

from model.salas import Sala
from repositories.sala_repository import SalaRepository
from repositories.user_repository import UserRepository

from model.users import User

from model.users import User

class SalaService:
    def __init__(self):
        self.salaRepository = SalaRepository()
        self.userRepository = UserRepository()
    
    def mover(self, user: User) -> Optional[User]:
        
        salaAtual = self.salaRepository.salaAtual(user)
        
        inp = input("Você possui as seguintes opções:\n" +
                "L - Leste: Sala " + str(salaAtual.destinos[0]) + "\n" +
                "O - Oeste: Sala " + str(salaAtual.destinos[1]) + "\n" +
                "N - Norte: Sala " + str(salaAtual.destinos[2]) + "\n" +
                "S - Sul: Sala " + str(salaAtual.destinos[3]) + "\n"
                "Digite sua escolha: ")
        
        if inp == 'l' or inp == 'L':
            self.salaRepository.updateSala(user, salaAtual.destinos[0])
        elif inp == 'o' or inp == 'O':
            self.salaRepository.updateSala(user, salaAtual.destinos[1])
        elif inp == 'n' or inp == 'N':
            self.salaRepository.updateSala(user, salaAtual.destinos[2])
        elif inp == 'o' or inp == 'O':
            self.salaRepository.updateSala(user, salaAtual.destinos[3])

        user = self.userRepository.findUserByName(user.nome)

        print(user)

        return user

