numero = input("Informe o número: ")
base = int(input("Informe a base: "))

decimal = 0 
potencia = len(numero)-1

for digito in numero:
    decimal += int(digito)*(base**potencia)
    potencia-=1
print(f"Numero na base decimal {decimal}")