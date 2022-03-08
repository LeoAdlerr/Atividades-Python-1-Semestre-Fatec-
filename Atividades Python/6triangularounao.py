print("digite um número para desconbrir se ele é triangular ou não")
n1 = int(input('Entre com o número: '))
i = 1
t = 0
while t < n1:
	t = i*(i+1)*(i+2)
	i += 1

if t == n1:
	print('%d é triangular' %n1)
else:
	print('%d não é triangular' %n1)