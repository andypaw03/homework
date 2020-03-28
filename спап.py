file=open("Вайна и мир.txt","r", encoding="UTF-8")
b=0
for i in file:
    i=i.strip()
    i=i.split()
    line=[]
    for j in i:
        line.append(j.lower())
    b+=line.count("он")
file.close()
print(b)