class Instancia():
    def __init__(self, nome):
        self.nome =  nome #protudo ex

    def get(self, bd): #lista produtos do banco
        return bd.fetch("SELECT * FROM "+self.nome, None)

    def insert(self, bd, data):
        return bd.insert("INSERT INTO "+self.nome+" VALUES (NULL, "+data+")", None)

    def update(self, bd, id, data):
        return bd.update("UPDATE "+self.nome+" SET data = '"+str(data)+"' WHERE id = "+str(id), None)
        
    def delete(self, bd, id):
        return bd.delete("DELETE FROM "+self.nome+" WHERE id = "+str(id), None)

    def getById(self, bd, id):
        return bd.fetchone("SELECT * FROM "+self.nome+" WHERE id = "+str(id), None)

    def getFKReference(self, bd, fk, tabela_alvo):
        return bd.fetchone("SELECT * FROM "+tabela_alvo+" WHERE id = "+str(fk), None)
