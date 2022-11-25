from database.instancia import Instancia
from classes.venda import Venda
from classes.usuario import Usuario
from classes.gerente import Gerente
from classes.utils import *

class ListaVendas(Instancia):
    def __init__(self):
        super().__init__('vendas')
        self.vendas = []
    
    def set(self, bd):
        self.vendas = []
        lista = self.get(bd)
        for i in lista:
            usuario = self.getUsuario(i[1], bd)
            self.vendas.append(Venda(i[0], usuario))

    def getUsuario(self, id, bd):
        res = self.getFKReference(bd, id, 'usuarios')
        if res[3] == 0:
            return Usuario(res[0], res[1], res[2])
        return Gerente(res[0], res[1], res[2])

    def addVenda(self, bd, usuario):
        data = "'"+str(usuario.id)+"'"
        self.insert(bd, data)
        self.vendas.append(Venda(None, usuario))

    def getVendaNaoFinalizada(self):
        for venda in self.vendas:
            if venda.data == 0:
                print('\n\nVenda não finalizada encontrada!')
                print('Vendedor: '+venda.vendedor.nome)
                print('Total: '+str(venda.total))
                print('Id: '+str(venda.id))
                for produto in venda.lista_produtos:
                    print('Produto: '+produto.nome)
                    print('Preço: '+str(produto.preco))

    def finalizarVenda(self, bd):
        id = valor_obrigatorio('Id da venda: ')
        for venda in self.vendas:
            if venda.id == id:
                venda.setVenda()
                self.update(bd, venda.id, venda.data)
                return venda
        return None