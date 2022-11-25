from database.listaProdutos import ListaProdutos
from database.listaLaboratorios import ListaLaboratorios
from database.listaUsuarios import ListaUsuarios

from classes.usuario import Usuario

class Session():
    def __init__(self, bd):
        self.usuario = None
        self.lista_produtos = ListaProdutos() #Quando cria uma lista de produtos, ela cria uma instancia
        self.lista_laboratorios = ListaLaboratorios()
        self.lista_usuarios = ListaUsuarios()

        self.bd = bd
        self.refresh()

    def refresh(self):
        self.lista_produtos.set(self.bd) #puxa os dados do banco e cria os objetos
        self.lista_laboratorios.set(self.bd) #puxa os dados do banco e cria os objetos
        self.lista_usuarios.set(self.bd) #puxa os dados do banco e cria os objetos

    def setUsuario(self, usuario):
        self.usuario = usuario


