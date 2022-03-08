voto = 0

total_candidato1 = 0
total_candidato2 = 0
total_candidato3 = 0
total_candidato4 = 0
total_nulos = 0
total_brancos = 0
total_geral = 0

while True:
    print('Informe:')
    print('1, 2, 3, 4 para votar no seu respectivo candidato')
    print('5 para votar nulo')
    print('6 para votar em branco')
    print('0 para encerrar a votação')
    voto = int(input('Qual o seu voto? '))

    if voto == 0:
        break

    if voto == 1:
        total_candidato1 += 1
    elif voto == 2:
        total_candidato2 += 1
    elif voto == 3:
        total_candidato3 += 1
    elif voto == 4:
        total_candidato4 += 1
    elif voto == 5:
        total_nulos += 1
    elif voto == 6:
        total_brancos += 1
    total_geral += 1

# --- Votos e percentual de cada candidato
print(f'Numero de votos do candidato 1: {total_candidato1} - Percentual: {(total_candidato1/total_geral)*100:.2f}')
print(f'Numero de votos do candidato 2: {total_candidato2} - Percentual: {(total_candidato2/total_geral)*100:.2f}')
print(f'Numero de votos do candidato 3: {total_candidato3} - Percentual: {(total_candidato3/total_geral)*100:.2f}')
print(f'Numero de votos do candidato 4: {total_candidato4} - Percentual: {(total_candidato4/total_geral)*100:.2f}')
# --- Votos e percentual nulos
print(f'Numero de votos nulos {total_nulos} - Percentual: {(total_nulos/total_geral)*100:.2f}')
# --- Votos e percentual brancos
print(f'Numero de votos brancos {total_brancos} - Percentual: {(total_brancos/total_geral)*100:.2f}')