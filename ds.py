a=input("")
b=0
c=0
while b<len(a):
    if a[b]=="2" or a[b]=="k" or a[b]=="o" or a[b]=="f":
        c+=1
    b+=1
print (c)
