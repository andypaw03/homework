a=[None, 'ssdvsdv', 34, 2, '2', '234567898765', [1, 2, 3, 4], 9]
func1=lambda x: True if x is None else False
func2=lambda y: y if len(str(y))>=8.1246 else " "
b=[]
for i in a:
    if func1(i):
        continue
    b.append(func2(i))
print(b)
