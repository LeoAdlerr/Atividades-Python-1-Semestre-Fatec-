# Estruturas de Repetição
# ENQUANTO...FAÇA -> WHILE (Python)
# FAÇA...ENQUANTO -> DO...WHILE (Não existe Python - NP)
# REPITA...ATÉ ->  REPEAT...UNTIL (Object Pascal) (NP)
# PARA var DE init...finish FAÇA -> FOR (Python)
# PARA var EM estrutura FAÇA -> FOR...IN (Python)
def is_valid(num):
    return True

a = 34
b = 13
while a > b and b < 60:
    print('Level 1')
    while b < 10:
        print('Level 2')
    b += 1
print('Test')
# --------------------------------
# for(inicializacao; condicional; incremento/decremento) {}
# for (int i = 0; i < 100; i++) {}
for index in range(0, 100, 2): # [1, 2, 3, ..., 20]
    print(index)
for index in range(100, 1, -2): # [1, 2, 3, ..., 20]
    print(index)
# --------------------------------
# Pandas, scipy, numpy, etc
#   Estendidas através de outras class
#   Exemplo: DataSet (Pandas)
# lists*, sets, dicts*, tuples
list_elements = [1, 2, 56, 78, 45, 90]
print(type(list_elements))
for element in list_elements:
    if element > 70:
        continue
    print(element)
    # break - Força uma quebra/saída da estrutura
    #         de repetição pai (um nível acima apenas)
    # continue - Força um retorno na análise da condição
    #            da estrutura

print('After break statement')



