def fib(number):
    if number == 0:
        return 0
    if number < 3:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
    
print fib(6)