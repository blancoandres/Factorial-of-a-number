n = int(input("Escriba un numero para sacar su factorial: "))
if n == 0:
    print(1)
m = 1
while n > 0:
    for i in range(n):
        m= m * n
        n = n - 1
        print(m)