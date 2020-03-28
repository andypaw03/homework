def fact(x):
    if x==1:
        return 1
    return x*fact(x-1)
a=fact(7)
print(a)
b=fact(4)
print(b)
