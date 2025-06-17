import math
contador = 0
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
mdc = math.gcd(a, b)
for i in range(1, mdc+1):
    if a % i == 0 and b % i ==0:
        contador+=1
        print(f"{i}")
print(f"MDC: {mdc}")
print(f"Tatal de divisores: {contador}")
