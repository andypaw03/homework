a=input("")
def func(x):
    b=0
    x=x.lower()
    for i in x:
        if i in "aeiou":
            b+=1
    return b
print(func(a))
