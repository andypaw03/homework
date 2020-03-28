a=input("").split()
b=[""]
for i in range(len(a)):
    minn=a[0]
    for j in a:
        if minn>j:
            minn=list(j)
    a.remove(minn)
    b.append(minn)
print(b)
