class Inventario:
    def __init__(self,tamanho_inventario, momento_coleta_Item, id_item, id_jogador, id=None):
        self.id = id
        self.tamanho_inventario = tamanho_inventario
        self.momento_coleta_Item = momento_coleta_Item
        self.id_item = id_item
        self.id_jogador = id_jogador
        
    def __str__(self):
        return f"Inventario[id={self.id}, tamanho_inventario={self.tamanho_inventario}, momento_coleta_Item={self.momento_coleta_Item}, id_item={self.id_item}, id_jogador={self.id_jogador}]"
