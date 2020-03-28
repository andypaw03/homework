with open("hl.txt","r", encoding="UTF-8")as file:
    b=0
    for i in file:

        line=[]
        for j in i:
            line.append(j.lower())
        b+=line.count("=")

print(b)