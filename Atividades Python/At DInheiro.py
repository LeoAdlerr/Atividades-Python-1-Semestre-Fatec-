def solucaoanagrama(s1,s2):
    umalista = list(s2)

    pos1 = 0
    aindaOK = True

    while pos1 < len(s1) and aindaOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(umalista) and not encontrado:
            if s1[pos1] == umalista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            umalista[pos2] = None
        else:
            aindaOK = False

        pos1 = pos1 + 1

    return aindaOK
x = input("s1: ")
x1 = input("s2: ")
print(solucaoanagrama(x, x1))
import time
def troco():
    dinheroapagar = float(input("Dinheiro a Pagar:R$ "))
    dinheirorecebido = float(input("Dinheiro Recebido:R$ "))
    if dinheroapagar == dinheirorecebido:
        print("O dinheiro a pagar é igual ao dinheiro recebido.")
    elif dinheirorecebido < dinheroapagar:
        print("ERRO!!!\n O valor recebido é inferior ao valor a pagar")
    else:
        troco = dinheirorecebido - dinheroapagar
        trocoarrendando = round(troco, 2)
        time.sleep(5)
        print("\n\n\tO Valor do troco é de {} reais".format(trocoarrendando))


def sair ():
    quit()

def menu():
    escolha = input(""" 
                A: Calcular o Troco
                B: Sair
                Escolha uma hipótese: 
    """)
    escolha = escolha.lower()
    if escolha == 'a':
        troco()
        time.sleep(5)
        menu()
    elif escolha == 'b':
        time.sleep(5)
        sair()
    else:
        print("Erro na Tecla!")
        print("Por favor, escolha novamente.")
        menu()
menu()
L = [1, 7, 4, 12, -2]
x = L[0]
while True:
    L = L[1:]
    if not L:
        break
    if L[0] > x:
        x = L[0]
print (x)