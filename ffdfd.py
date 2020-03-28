def fact(x):
    if x==1:
        return 3
    return 2*fact(x-1)
for i in range(1,1000):
    a=fact(i)
    print(a)
    
