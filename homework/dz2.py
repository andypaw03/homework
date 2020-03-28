a=0
def fib(x):
    if x < 3 & x > 0:
        return 1
    if x <= 0:
        return 0
    return fib(x - 1) + fib(x - 2)
def gen(y):
    for i in range(y, 30):
        print(fib(y))
        y += 1
while True:
    print(next(gen(a)))
