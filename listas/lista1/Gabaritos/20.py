total = 0
n = 6
while(total <4):
    soma = sum(i for i in range(1,n) if n%i==0)
    if soma == n:
        total+=1
        print(f"{n}")
    n+=1

