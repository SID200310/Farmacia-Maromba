import datetime
from classes.produto import Produto

class Venda:
    def __init__(self, id, vendedor):
        self.id = id
        self.lista_produtos = []
        self.total = 0
        self.vendedor = vendedor
        self.data = 0

    def add(self, produto):
        self.lista_produtos.append(produto)
        self.total += produto.preco
    
    def setVenda(self):
        self.lista_produtos = []
        self.data = datetime.datetime.now()