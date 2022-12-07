def fib(f):
    if f == 1 or f == 2:
        return 1 
    else:
        return fib(f-1) + fib(f-2)

print(fib(6))