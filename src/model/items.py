class Item:
    def __init__(self, nome, descricao, tipo, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        
    def __str__(self):
        return f"Item[id={self.id}, nome={self.nome}, descricao={self.descricao}, tipo={self.tipo}]"
