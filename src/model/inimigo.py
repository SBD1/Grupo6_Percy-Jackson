class Inimigo:
    def __init__(self, vida,ataque, time_ataque, id=None):
        self.id = id
        self.vida = vida
        self.ataque = ataque
        self.time_ataque = time_ataque
        
    def __str__(self):
        return f"Inimigo[id={self.id}, vida={self.vida}, ataque={self.ataque}, time_ataque={self.time_ataque}]"
