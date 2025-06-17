D1 = int(input("Informe o 1º dia: "))
M1 = int(input("Informe o 1º mês: "))
A1 = int(input("Informe o 1º ano: "))

D2 = int(input("Informe o 2º dia: "))
M2 = int(input("Informe o 2º mês: "))
A2 = int(input("Informe o 2º ano: "))

meses = [31,28,31,30,31,30,31,31,30,31,30,31]

total1 = D1
total2 = D2

for m in range(1,M1):
    if m ==2:
        if(A1 % 4 == 0 and A1 % 100 !=0) or (A1%400==0):
            total1 += 29
        else:
            total1 += 28
    else:
        total1 += meses[m-1] 

total1 += A1*365

for a in range (1, A1):
    if(a % 4 == 0 and a % 100 !=0) or (a%400==0):
        total1+=1

for m in range(1,M2):
    if m ==2:
        if(A1 % 4 == 0 and A1 % 100 !=0) or (A1%400==0):
            total2 += 29
        else:
            total2 += 28
    else:
        total2 += meses[m-1] 

total2 += A2*365

for a in range (1, A2):
    if(a % 4 == 0 and a % 100 !=0) or (a%400==0):
        total2+=1

print(f"Quantidade de dias: ", abs(total2-total1))
