nome1 = input("Informe o nome do país 1: ")
ouro1 = int(input("Informe o número de medalhas de ouro do país 1: "))
prata1 = int(input("Informe o número de medalhas de prata do país 1: "))
bronze1 = int(input("Informe o número de medalhas de bronze do país 1: "))
peso1 = (ouro1 * 3) + (prata1 * 2) + (bronze1 * 1)

nome2 = input("Informe o nome do país 2: ")
ouro2 = int(input("Informe o número de medalhas de ouro do país 2: "))
prata2 = int(input("Informe o número de medalhas de prata do país 2: "))
bronze2 = int(input("Informe o número de medalhas de bronze do país 2: "))
peso2 = (ouro2 * 3) + (prata2 * 2) + (bronze2 * 1)

nome3 = input("Informe o nome do país 3: ")
ouro3 = int(input("Informe o número de medalhas de ouro do país 3: "))
prata3 = int(input("Informe o número de medalhas de prata do país 3: "))
bronze3 = int(input("Informe o número de medalhas de bronze do país 3: "))
peso3 = (ouro3 * 3) + (prata3 * 2) + (bronze3 * 1)

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3:
        print("Países: 1(%d) - 2(%d) - 3(%d)" %(peso1, peso2, peso3))
    elif peso3 > peso2:
        print("Países: 1(%d) - 3(%d) - 2(%d)" % (peso1, peso3, peso2))
    else:
        print("Países: 1(%d) - Empate entre 2(%d) e 3(%d)" % (peso1, peso2, peso3))
elif peso2 > peso1 and peso2 > peso3:
    if peso1 > peso3:
        print("Países: 2(%d) - 1(%d) - 3(%d)" %(peso2, peso1, peso3))
    elif peso3 > peso1:
        print("Países: 2(%d) - 3(%d) - 1(%d)" % (peso2, peso3, peso1))
    else:
        print("Países: 2(%d) - Empate entre 1(%d) e 3(%d)" % (peso2, peso1, peso3))
elif peso3 > peso1 and peso3 > peso2:
    if peso1 > peso2:
        print("Países: 3(%d) - 1(%d) - 2(%d)" %(peso3, peso1, peso2))
    elif peso2 > peso1:
        print("Países: 3(%d) - 2(%d) - 1(%d)" % (peso3, peso2, peso1))
    else:
        print("Países: 3(%d) - Empate entre 1(%d) e 2(%d)" % (peso3, peso1, peso2))
else:
    print("Empate geral")