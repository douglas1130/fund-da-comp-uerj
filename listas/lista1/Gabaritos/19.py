soma=0
n = int(input("Digite um número: "))
for i in range(n-1, 0, -1):
    if n % i == 0:
        print(f"{i}")
        soma+=i
print(f"{n} é perfeito, pois a soma é {soma}")