a=input("")
b=0
for i in range(int(a)):
    if a[i] in "+-*/":
        first=a[:i]
        second=a[i+1:]
        what_to_do=a[i]
        break
if what_to_do=="+":
        print(int(first)+int(second))
if what_to_do=="-":
        print(int(first)-int(second))
if what_to_do=="*":
        print(int(first)*int(second))
if what_to_do=="/" and not what_to_do== "0":
    print(int(first)/int(second))
else:
    print("NO! GOD PLEASE NOOO!!!!!!")
