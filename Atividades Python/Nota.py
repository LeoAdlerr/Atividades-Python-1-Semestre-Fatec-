def leiaInt(msg):
    ok = False
    valor = [0,1,2,3,4,5,6,7,8,9,10]
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt("digite um número: ")
print(f'Você acabou de digitar o número {n}')








