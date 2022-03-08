nota = -1

while nota < 0 or nota > 10:
    nota = int(input("\033[036mInforme a nota entre 0 e 10\033[m (\033[035mapenas valores inteiros e dentro das especificações!\033[m): "))
    if nota < 0 or nota > 10:
        print("\033[031mValor inválido!\033[m")
    elif nota >= 0 or nota <= 10:
        print(f"Nota do aluno = {nota}")
        break
