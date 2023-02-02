class Boss:
    def __init__(self, multi_vida,multi_ataque, id_nivel, id=None):
        self.id = id
        self.multi_vida = multi_vida
        self.multi_ataque = multi_ataque
        self.id_nivel = id_nivel
        
    def __str__(self):
        return f"Boss[id={self.id}, multi_vida={self.multi_vida}, multi_ataque={self.multi_ataque}, id_nivel={self.id_nivel}]"
