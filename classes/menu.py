from classes.listas import Session
from classes.utils import *
from database.bd_connector import BDConnector

bd = BDConnector({
    'host': 'localhost',
    'user': 'root',
    'password' : '',
    'database': 'farmaciamaromba'
})

sessao = None

def main():
    sessao = Session(bd)
    clear()
    while True:
        print('Bem vindo ao sistema de gerenciamento da Farmácia Maromba!')
        escreva("Para poder acessar o sistema, voce precisa se autenticar", "amarelo")
        print("Caso nao tenha uma conta, crie uma antes")
        print("0 - Sair")
        print("1 - Logar")
        print("2 - Criar conta")
        opcao = input("\nDigite a opcao desejada: ")
        clear()
        print('\n')
        if opcao == "0":
            exit()
        elif opcao == "1":
            usuario = sessao.lista_usuarios.auth()
            if usuario == None:
                escreva("Usuario ou senha incorretos", "vermelho")
            else:
                sessao.setUsuario(usuario)
                usuario.menu(sessao)
        elif opcao == "2":
            sessao.lista_usuarios.addUsuario(bd)
            escreva("Faça o login agora", "verde")
                