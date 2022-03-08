idade = int(input("Informe sua idade: "))

if idade < 16:
    classe = "não votante"
elif idade < 18 or idade > 65:
    classe = "eleitor facultativo"
elif idade > 17 or idade < 66:
    classe = "eleitor obrigatório"

print("Trata-se de %s." %classe)