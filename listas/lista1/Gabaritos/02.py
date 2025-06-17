primeiro = int(input("Primerio termo da PA: "))
razao = int(input("Informe a razão da PA: "))
n = int(input("Quantidade de termos: "))

for i in range(n):
    termo = primeiro + i * razao
    print(termo )

