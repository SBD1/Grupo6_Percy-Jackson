import sys
import os

from typing import Optional
from service.user_service import UserService

def clear():
    os.system('cls')


class Main:

    def __init__(self):
        self.userService = UserService()
        self.activeUser = None
        
    def start(self):

        print("______                       ___            _                    ")
        print("| ___ \                     |_  |          | |                   ")
        print("| |_/ /__ _ __ ___ _   _      | | __ _  ___| | _____  ___  _ __  ")
        print("|  __/ _ \ '__/ __| | | |     | |/ _` |/ __| |/ / __|/ _ \| '_ \ ")
        print("| | |  __/ | | (__| |_| | /\__/ / (_| | (__|   <\__ \ (_) | | | |")
        print("\_|  \___|_|  \___|\__, | \____/ \__,_|\___|_|\_\___/\___/|_| |_|")
        print("                    __/ |                                        ")
        print("                   |___/                                       \n")

        print('Escolha uma das opções abaixo(1-3):\n')

        print('1 - Criar Novo Personagem\n' +
              '2 - Carregar Personagem\n' +
              '3 - Sair\n\n\n')

        print('Digite a opção desejada: \n')

        inp = 0

        while (inp not in [1, 2, 3]):
            inp = input('> ')

            if inp == '1':
                self.activeUser = self.userService.create()
                self.play()
                

            if inp == '2':
                self.activeUser = self.userService.login()
                self.play()

            if inp == '3':
                sys.exit()
                break

            else:
                print('\nOpção Inválida!')


    def play(self) -> Optional[bool]:
        print(f'Login bem-sucedido no personagem {self.activeUser}')
        exit = input('Digite qualquer coisa para sair: ')
        if exit is not None:
            return False
    
if __name__ == '__main__':
    game = Main()
    game.start()