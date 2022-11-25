from classes.usuario import Usuario
from classes.utils import *

class Gerente(Usuario):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha)
        self.gerente = True
    
    def eGerente(self):
        return self.gerente

    def menuUsuario(self, sessao):
        super().menuUsuario(sessao)
        print("\n\n1 - Cadastrar Usuario \n2 - Listar Usuarios \n3 - Remover Usuario \n4 - Voltar")
        opcao = input("Digite a opcao desejada: ")
        clear()
        sessao.refresh()
        if opcao == '1':
            sessao.lista_usuarios.addUsuario(sessao.bd)
        elif opcao == '2':
            lista = sessao.lista_usuarios.getUsuarios()
            for usuario in lista:
                usuario.descreva()
        elif opcao == '3':
            sessao.lista_usuarios.removerUsuario(sessao.bd)
        else:
            print("Opcao invalida")
            return False



    