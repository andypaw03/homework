a=input(" ")
b=0
while True:
    c=a[b]
    if not c.isdigit() and"?"!=c and "-"!=c:
        print(c)
    break
