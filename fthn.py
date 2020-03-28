while True:
    a=input("VVedite slovo")
    
    if len(a)%2==0:
        b=a[::-1]
        print(b)
    if len(a)%2!=0:
        c=a[0::-1]
        print(c)
