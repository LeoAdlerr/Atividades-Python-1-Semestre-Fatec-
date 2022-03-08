import math
a= float(input("valor de a"))
b= float(input("valor de b"))
c= float(input("valor de c"))
Delta=(b**2)-(4*a*c)

if Delta<0:print("raiz negativa inexistente")

else: X=math.sqrt(Delta)
X1=(-b+X)/(2*a)
X2=(-b-X)/(2*a)
print(X1)
print(X2)