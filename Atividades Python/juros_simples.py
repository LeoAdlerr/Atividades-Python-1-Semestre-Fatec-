capital = float(input("Informe o capital"))
taxa_imprestimo = float(input("Informe a taxa de juros: "))
periodo_meses = int(input("Informe o nr. de meses: "))

juros_simples = capital * taxa_imprestimo * periodo_meses

print(f"O valor do juros calculado é de {juros_simples}.")