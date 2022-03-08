# Exercicio 25
num_elements = 5

H = 0.0
dividendo = 1
for divisor in range(1, num_elements + 1):
   H += dividendo / divisor
   dividendo += 2
print(f'O resultado da série H é {H:.2f}')
