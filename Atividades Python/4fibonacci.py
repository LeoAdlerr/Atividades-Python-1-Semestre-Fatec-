n = int(input("Número: "))
a = 1
b = 1
x = 1
while x <= (n-1): #n-1 pq começa do zero
    a, b = b, a+b
    x += 1

print(a)

