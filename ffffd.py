def drdr(file_name):
    with open(file_name,"r", encoding="UTF-8")as file:
        data=file.readlines()

    modified_data=[]
    for i in data:
        line=" "
        ch=0
        while ch < len(i):
            if i[ch]==" ":
                line+=" "
            else:
                break
            ch+=1
        subline=i.split()
        for j in subline:
            line+="kek"
        modified_data.append(line+"\n")
    with open(file_name,"w")as file:
        for i in modified_data:
            file.write(i)
kek_changer=("naw.py")