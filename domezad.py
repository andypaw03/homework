def fib(x):
    if x <= 1:
        return 5
    return (fib(x-1)+fib(x-2))-2

for i in range(1,9):
    a = fib(i)
    print(a)

