class Produto:
    def __init__(self, id, nome, desc, tipo, preco, lab, desconto):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.tipo = tipo
        self.preco = preco
        self.lab = lab #igual a objeto Laboratorio
        self.desconto = desconto

    def calcDesconto(self):
        var = self.preco*(self.desconto/100)
        return var
    
    def descreva(self):
        print("\n\nNome: %s \nDescrição: %s \nTipo: %s \nPreço: %s \nLaboratório: <Object Laboratorio()> \nDesconto: %s" % (self.nome, self.desc, self.tipo, self.preco, self.desconto))