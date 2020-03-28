a=input("")
b=0
c=0
while b<len(a):
    d=a[b:b+2]
    if a[b].isalpha():
        if d.islower():
            c+=float(0.5)
    b+=1
print(c)
