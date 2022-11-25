class Laboratorio:
    def __init__(self, id, nome, cnpj, tel, email):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.tel = tel
        self.email = email
    #get and set
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    def getCnpj(self):
        return self.cnpj
    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    def getTel(self):
        return self.tel
    def setTel(self, tel):
        self.tel = tel
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def __str__(self):
        return self.nome
    def __repr__(self):
        return self.nome

    def descreva(self):
        print("\n\nNome: %s \nCNPJ: %s \nTelefone: %s \nEmail: %s" % (self.nome, self.cnpj, self.tel, self.email))