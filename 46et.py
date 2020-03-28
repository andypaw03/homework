def fact(x):
    if x<=1:
        return 1
    return fact(x-1)+fact(x-2)
a=fact(7)
print(a)
    
