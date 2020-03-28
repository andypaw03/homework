def coh(file_name):
    with open(file_name,"r", encoding="UTF-8")as file:
        b=0
        for i in file:
            i=list(i)
            b+=i.count("=")
    return b
print(coh("hl.txt"))