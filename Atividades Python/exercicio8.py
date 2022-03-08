dia = int(input("Informe o dia (1...31): "))
mes = int(input("Informe o mês (1...12): "))
ano = int(input("Informe o ano: "))
valido = False

if ano >= 0:
    if mes == 1 and (dia >= 1 and dia <= 31):
        valido = True
    elif (mes == 2):
        if ((ano % 4) == 0 and (ano % 100) != 0) or (ano % 400) == 0:
            if dia >= 1 and dia <= 29:
                valido = True
        else:
            if dia >= 1 and dia <= 28:
                valido = True
    elif mes == 3 and (dia >= 1 and dia <= 31):
        valido = True
    elif mes == 4 and (dia >= 1 and dia <= 30):
        valido = True
    elif mes == 5 and (dia >= 1 and dia <= 31):
        valido = True
    elif mes == 6 and (dia >= 1 and dia <= 30):
        valido = True
    elif mes == 7 and (dia >= 1 and dia <= 31):
        valido = True
    elif mes == 8 and (dia >= 1 and dia <= 31):
        valido = True
    elif mes == 9 and (dia >= 1 and dia <= 30):
        valido = True
    elif mes == 10 and (dia >= 1 and dia <= 31):
        valido = True
    elif mes == 11 and (dia >= 1 and dia <= 30):
        valido = True
    elif mes == 12 and (dia >= 1 and dia <= 31):
        valido = True
print("A data informada é %s." %("válida" if valido else "inválida"))