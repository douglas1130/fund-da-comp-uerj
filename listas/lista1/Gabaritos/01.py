total_salario_homem = total_salario_mulher = 0
cont_homem = cont_mulher = 0
maior_salario_menorque30 = 0

while True:
    idade = int(input("Informe a idade: "))

    if(idade<0):
        break

    sexo = input("Informe o seu sexo (M/F): ")
    salario = float(input("Informe o salário: "))

    if (sexo=="M"):
        total_salario_homem += salario
        cont_homem +=1
    elif (sexo=="F"):
        total_salario_mulher += salario
        cont_mulher += 1
    else:
        print("Informe um sexo válido!")
        break

    if (idade < 30 and salario > maior_salario_menorque30):
        maior_salario_menorque30 = salario
        
media_salario_homem = total_salario_homem/cont_homem if cont_homem else 0
media_salario_mulher = total_salario_mulher/cont_mulher if cont_mulher else 0

print(f"O média salário de homem é R${media_salario_homem:.2f}")
print(f"O média salário de mulher é R${media_salario_mulher:.2f}")
print(f"O maior salário < 30 é R${maior_salario_menorque30:.2f}")
