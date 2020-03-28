a=input("")
b=""
for i in range(0, len(a)-1):
    first=a[0:i]
    if a[i]=="*":
        b=first*int(a[i+1:len(a)])
print(b)
