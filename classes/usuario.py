from classes.laboratorio import Laboratorio
from classes.utils import *
from classes.listas import *

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

    def login(self, senha_inserida):
        return self.senha == senha_inserida
    
    def eGerente(self):
        return False
    
    def descreva(self):
        print("\nid: %s \nNome: %s \nSenha: ****** " % (self.id, self.nome))

    def menuUsuario(self, sessao):
        return False

    def menuGerente(self, sessao):
        return False

    def menuProduto(self, sessao):
        print("\n\n1 - Cadastrar Produto \n2 - Listar Produtos \n3 - Remover Produto \n5 - Menu Usuario \n4 - Voltar")
        opcao = input("Digite a opcao desejada: ")
        clear()
        sessao.refresh()
        if opcao == '1':
            sessao.lista_produtos.addProduto(sessao.bd)
        elif opcao == '2':
            lista = sessao.lista_produtos.getProdutos()
            for produto in lista:
                produto.descreva()
        elif opcao == '3':
            sessao.lista_produtos.removerProduto(sessao.bd)
        elif opcao == '4':
            self.menu()
        else:
            print("Opcao invalida")
            return False


    def menu(self, sessao):
        print("\n\nBem vindo %s" % self.nome)
        while True:
            print("\n\n0 - Sair \n1 - Menu Produtos \n2 - Menu Vendas \n3 - Menu Usuarios")
            opcao = input("Digite a opcao desejada: ")
            clear()
            sessao.refresh()
            if opcao == '0':
                return False
            elif opcao == '1':
                self.menuProduto(sessao)
            elif opcao == '2':
                return 'menuVendas'
            elif opcao == '3':
                self.menuUsuario(sessao)
            else:
                print("Opcao invalida")

        