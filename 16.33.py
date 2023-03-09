def primes(m, n):
    while m <= n:
        is_prime = True
        for i in range(2, int(m**0.5)+1):
            if m % i == 0:
                is_prime = False
                break
        if is_prime and m > 1:
            yield m
            m += 1
        else:
            m += 1


if __name__ == '__main__':
    p = primes(100, 200)
    for x in p:
        print(x)