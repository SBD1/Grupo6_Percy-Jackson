from model.users import User
from model.inimigo import Inimigo
from repositories.sala_repository import SalaRepository
from model.comum import Comum
import time

class GeneralServices:
    def __init__(self):
        pass

    def lutar(self, user: User, inimigo: Comum):
        print(inimigo)
        print('Escolha uma das opções abaixo(1-2):\n')

        opcao = input('1 - Lutar\n' +
            '2 - Fugir\n\n\n' +
            'Digite a opção desejada: \n')

        if opcao == '1':
            
            while user.vida > 0 and inimigo.vida > 0:
                print('Você atacou o inimigo!')
                inimigo.vida -= user.ataque
                print(f'Vida do inimigo: {inimigo.vida}')
                time.sleep(2)
                print('O inimigo atacou você!')
                user.vida -= int(inimigo.ataque)
                print(f'Sua vida: {user.vida}')
                time.sleep(2)

            return print(inimigo)