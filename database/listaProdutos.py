from database.instancia import Instancia
from classes.produto import Produto
from classes.laboratorio import Laboratorio
from classes.utils import *

class ListaProdutos(Instancia):
    def __init__(self):
        super().__init__('produtos')
        self.produtos = []

    # Setar a lista de produtos com os dados do banco
    def set(self, bd):
        self.produtos = []
        lista = self.get(bd)
        for i in lista:
            laboratorio = self.getLaboratorio(i[5], bd)
            novo_produto = Produto(i[0], i[1], i[2], i[3], i[4], laboratorio, i[6])
            self.produtos.append(novo_produto)

    # Adiciona um produto no banco e na lista
    def addProduto(self, bd):
        nome = valor_obrigatorio("Nome")
        desc = valor_obrigatorio("Descrição")
        tipo = valor_obrigatorio("Tipo")
        preco = valor_obrigatorio("Preço")
        lab = valor_obrigatorio("Identificador do Laboratório")
        desconto = valor_obrigatorio("Desconto")

        laboratorio = self.getLaboratorio(lab, bd)
        novo_produto = Produto(None, nome, desc, tipo, preco, laboratorio, desconto)
        data = "'"+nome+"', '"+desc+"', '"+tipo+"', "+preco+", "+lab+", "+desconto
        self.insert(bd, data)
        self.produtos.append(novo_produto)

    # Remove um produto do banco e da lista
    def removerProduto(self, bd):
        print('\n\nRemovendo um produto!')
        self.getProdutoIdXNome()
        print('0- Cancelar')
        identificador = valor_obrigatorio("Identificador do produto")
        if identificador != '0':
            self.delete(bd, identificador)
            # buscar na lista o produto com o id e remover
            for produto in self.produtos:
                if produto.id == identificador:
                    self.produtos.remove(produto)
                    break

    # Busca um laboratório pelo id
    def getLaboratorio(self, id, bd):
        res = self.getFKReference(bd, id, 'laboratorios')
        return Laboratorio(res[0], res[1], res[2], res[3], res[4])

    # Retorna uma lista com os produtos e seus respectivos ids
    def getProdutoIdXNome(self):
        for produto in self.produtos:
            print(str(produto.id) + '- ' + str(produto.nome)+'.')

    # Retorna a lista de produtos
    def getProdutos(self):
        return self.produtos