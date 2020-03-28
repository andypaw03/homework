zad=["р","а","д","у","г","а"]
slov=[]
neugad=[]
b=0
a=list(input(""))
while  True:
    print("не угаданные-",neugad)
    if a[b]=="р":
        slov.append("р")
    elif a[b]=="а":
        slov.append("а")
    elif a[b]=="д":
        slov.append("д")
    elif a[b]=="у":
        slov.append("у")
    elif a[b]=="г":
        slov.append("г")
    elif a[b]=="а":
        slov.append("а")
    if a[b]==zad[b] and len(neugad)==0:
        print('  ___\n')
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    elif a[b]==zad[b] and len(neugad)==1:
        print( "  ___\n |     |\n")
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    elif a[b]==zad[b] and len(neugad)==2:
        print("  ___\n |     |\n |    0\n")
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    elif a[b]==zad[b] and len(neugad)==3:
        print("  ___\n |     |\n |    0\n |   /|\\\n")
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    elif a[b]==zad[b] and len(neugad)==4:
        print("  ___\n |     |\n |    0\n |   /|\\\n |   / \\\n")
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    elif a[b]==zad[b] and len(neugad)==5:
        print("  ___\n |     |\n |    0\n |   /|\\\n |   / \\\n/|\\")
        neugad+=a
        print("не угаданные-",neugad)
        print("угаданные-",slov)
        
    if slov==zad:
        print("Ты выграл")
        break
    
    if len(neugad)==6:
        print("Ты проиграл")
        break
