a=input("")
b=0
c=""
d=""
while b<len(a):
    if len(a)%2:

        c+=a[b]
    else:
        d+=a[b]
    b+=1
print(c+d)
