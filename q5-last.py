def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(i)
            n = n/i
    if n > 1:
        factors.append(n)
    return factors

numbers= int(input("number: "))
prime_factors = prime_factors(numbers)
print(prime_factors)
