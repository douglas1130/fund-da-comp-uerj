pares = impares = soma_par = 0

while True:
    num = int(input("Informe o número: "))
    if num == 0 :
        break
    elif num % 2 == 0:
        pares += 1
        soma_par += num
    else:
        impares += 1

media_par = soma_par/pares if pares else 0
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Média Pares: {media_par:.2f1}")
