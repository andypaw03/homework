a=['sdvicsdv', 78, [2, 56], 'sdfbsfdb', None, None, 'None', 3456789, 'None2']
func1=lambda x: True if x is None else False
func2=lambda y: y if len(str(y))>=5 else " "
b=[]
for i in a:
    if func1(i):
        continue
    b.append(func2(i))
print(b)
