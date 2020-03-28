a="a,b,c,d"
b="a,b,c"
x=lambda a, b: a if len(a)>=len(b) else b
answ= x(a,b)
print(answ)