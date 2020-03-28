a=input("")
def func(x):
    c=""
    x=x.lower()
    for i in x:
        if i not in "aeiou":
            c+=i
    return c
print(func(a))
