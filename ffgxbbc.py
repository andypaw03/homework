a1 = a2 = 1
 
m = int(input("максимальное число: ")) + 1
 
while a1 <= m:
    a1, a2 = a2, a1 + a2
    m -= 1
    print(a1)
