dia = int(input("Informe um dia (1...31): "))
mes = int(input("Informe um mês (1...12): "))
signo = ""

if (mes == 3 and dia >=21) or (mes == 4 and dia <= 19):
    signo = "ÁRIES"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "TOURO"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "GÊMEOS"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "CÂNCER"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "LEÃO"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "VIRGEM"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "LIBRA"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "ESCORPIÃO"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "SAGITÁRIO"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "CAPRICÓRNIO"
elif (mes == 1 and dia >= 22) or (mes == 2 and dia <= 18):
    signo = "ÁQUARIUS"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "PEIXES"
else:
    signo = "INVÁLIDO"

print("O signo referente à data é %s." %signo)