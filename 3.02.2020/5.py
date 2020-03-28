def func():
    i=0
    while True:
        if i%3==0 & i%5==0:
            yield i
            i+=1
x=func()
b=list(x)
print(next(x))