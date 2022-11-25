from database.instancia import Instancia
from classes.usuario import Usuario
from classes.gerente import Gerente
from classes.utils import *

senha_secreta = '123'

class ListaUsuarios(Instancia):
    def __init__(self):
        super().__init__('usuarios')
        self.usuarios = []
        self.gerentes = []

    def set(self, bd):
        self.usuarios = []
        self.gerentes = []
        lista = self.get(bd)
        for i in lista:
            if i[3] == 0:
                self.usuarios.append(Usuario(i[0], i[1], i[2]))
            else:
                self.gerentes.append(Gerente(i[0], i[1], i[2]))

    def auth(self):
        nome = valor_obrigatorio("Nome")
        senha = valor_obrigatorio("Senha")
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return usuario
        for gerente in self.gerentes:
            if gerente.nome == nome and gerente.senha == senha:
                return gerente
        print('Usuário não encontrado!')
        return None

    def addUsuario(self, bd):
        nome = valor_obrigatorio("Nome")
        senha = valor_obrigatorio("Senha")
        print('\nVocê é um gerente? Se sim, digite a senha secreta.')
        print('Ou apenas aperte enter para continuar.')
        gerente = input('Opção: ')
        if gerente == senha_secreta:
            print('Você criou com sucesso um gerencia padrão.')
            novo_usuario = Gerente(None, nome, senha)
            data = "'"+nome+"', '"+senha+"', 1"
            self.gerentes.append(novo_usuario)
        else:
            print('Você criou com sucesso um usuario padrão.')
            novo_usuario = Usuario(None, nome, senha)
            data = "'"+nome+"', '"+senha+"', 0"
            self.usuarios.append(novo_usuario)
        self.insert(bd, data)

    def removeUsuario(self, bd):
        print('Selecione o usuário:')
        for i in range(len(self.usuarios)):
            print(str(i+1)+'- '+self.usuarios[i].nome)
        id = valor_obrigatorio('número do usuário: ')
        self.delete(bd, id)
        return self.usuarios[id-1].id

    def removeGerente(self, bd):
        print('Selecione o gerente:')
        for i in range(len(self.gerentes)):
            print(str(i+1)+'- '+self.gerentes[i].nome)
        id = valor_obrigatorio('número do gerente: ')
        self.delete(bd, id)
        return self.gerentes[id-1].id

    def getUsuarios(self):
        return self.usuarios

    def getGerentes(self):
        return self.gerentes