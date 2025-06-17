A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))

if A>=B:
    print("Não é possível fazer a soma")
else:
    soma = sum(i for i in range(A+1, B))
    print(f"Somatório:{soma}")


