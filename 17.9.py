def decorator(maximum):
    cache = [None for _ in range(maximum)]

    def _decorator(func):

        def __decorator(arg: int, **kw):
            if arg > maximum:
                return f'Out of range ({arg})'

            if cache[arg-1] != None:
                return f'Already in cache: {cache[arg-1]}'
            else:
                y = func(arg, **kw)
                cache[arg-1] = y
                return y
            
        return __decorator
    
    return _decorator


@ decorator(10)
def fib(n, f0=1, f1=1, count=1):
    if count < n:
        return fib(n, f0=f1, f1=f0+f1, count=count+1)
    return f1

if __name__ == '__main__':
    print(fib(5))
    print(fib(5))
    print(fib(11))