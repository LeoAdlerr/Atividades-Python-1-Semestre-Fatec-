n = int(input('Entre com o número: '))

divisores = []
d = 2
while n > 1:
	if n%d == 0:
		n = n/d
		divisores.append(d)
	else:
		d += 1

print(divisores)