a=input("")
for i in a:
    b=a[i:-1:1]
    b+a[b]
print (b)
