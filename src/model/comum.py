from model.inimigo import Inimigo

class Comum(Inimigo):
    def __init__(self, id, id_inimigo, nome, fala, id_sala, vida, ataque):
        super().__init__(nome, fala, id_sala, vida, ataque)
        self.id
        self.id_inimigo = id_inimigo
    
    def __str__(self):
        return f"Comum[id={self.id}, id_inimigo={self.id_inimigo}, id_npc={self.id_npc}]"