a=['asdadf', 'qwe', 'tutytu']
b=['qweq', 'edgfhjasvc', 'sdssssssssss']
c=[]
func =lambda a,b:a if len(a)<=len(b) else b
for i in range(len(a)):
    c.append(func(a[i],b[i]))
print(c)