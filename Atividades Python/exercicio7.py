mes = int(input("Informe o identificador do mês (1...12): "))
mes_extenso = ""
if mes == 1:
    mes_extenso = "JANEIRO"
elif mes == 2:
    mes_extenso = "FEVEREIRO"
elif mes == 3:
    mes_extenso = "MARÇO"
elif mes == 4:
    mes_extenso = "ABRIL"
elif mes == 5:
    mes_extenso = "MAIO"
elif mes == 6:
    mes_extenso = "JUNHO"
elif mes == 7:
    mes_extenso = "JULHO"
elif mes == 8:
    mes_extenso = "AGOSTO"
elif mes == 9:
    mes_extenso = "SETEMBRO"
elif mes == 10:
    mes_extenso = "OUTUBRO"
elif mes == 11:
    mes_extenso = "NOVEMBRO"
elif mes == 12:
    mes_extenso = "DEZEMBRO"
else:
    mes_extenso = "INVÁLIDO"

print("O mês informado é %s." %mes_extenso)