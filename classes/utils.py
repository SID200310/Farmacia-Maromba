import os

#colors for the terminal
colors = {
    'schalata': '\033[95m',
    'azul': '\033[94m',
    'verde': '\033[92m',
    'amarelo': '\033[93m',
    'vermelho': '\033[91m',
    'fim': '\033[0m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m'
}

def escreva(texto, cor):
    print(colors[cor]+str(texto)+colors['fim'])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def valor_obrigatorio(nome_campo):
    while True:
        valor = input('\n'+str(nome_campo)+': ')
        if valor != '' and valor != ' ' and valor != None:
            return valor
        print("O valor %s é obrigatório! Tente novamente..." % nome_campo)