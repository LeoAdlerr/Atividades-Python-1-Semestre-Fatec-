lista = [11, 13, 14, 16, 17, 18, 19, 20]

def encontrarsolução(passo):
    for num in range(passo, 999999999, passo):
        if all(num % n == 0 for n in lista):
            return num
    return None

if __name__ == '__main__':
    solução = encontrarsolução(20)
    if solução is None:
        print("Nenhuma resposta encontrada :(")
    else:
        print(f"Resposta encontrada!: {solução}")