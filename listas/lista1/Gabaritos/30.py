A = int(input("Informe o número: "))
d = 2
while A > 1:
    e = 0
    while A%d==0:
        A//=d
        e +=1
    if e > 0:
        print(f"{d} ^ {e}")
    d+=1 
