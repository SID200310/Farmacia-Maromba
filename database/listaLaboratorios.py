from database.instancia import Instancia
from classes.laboratorio import Laboratorio
from classes.utils import *

class ListaLaboratorios(Instancia):
    def __init__(self):
        super().__init__('laboratorios')
        self.laboratorios = []
    
    def set(self, bd):
        self.laboratorios = []
        lista = self.get(bd)
        for i in lista:
            self.laboratorios.append(Laboratorio(i[0], i[1], i[2], i[3], i[4]))

    def getLaboratorios(self):
        return self.laboratorios

    def addLaboratorio(self, bd):
        nome = valor_obrigatorio("Nome")
        cnpj = valor_obrigatorio("CNPJ")
        endereco = valor_obrigatorio("Endereço")
        telefone = valor_obrigatorio("Telefone")
        email = valor_obrigatorio("Email")

        novo_laboratorio = Laboratorio(None, nome, cnpj, endereco, telefone, email)
        data = "'"+nome+"', '"+cnpj+"', '"+endereco+"', '"+telefone+"', '"+email+"'"
        self.insert(bd, data)
        self.laboratorios.append(novo_laboratorio)

    def removeLaboratorio(self, bd):
        print('Selecione o laboratório:')
        for i in range(len(self.laboratorios)):
            print(str(i+1)+'- '+self.laboratorios[i].nome)
        id = valor_obrigatorio('número do laboratório: ')
        self.delete(bd, id)
        return self.laboratorios[id-1].id