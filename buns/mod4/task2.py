def power(a, n):
    if n < 0:
        return 1 / power(a, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return a
    else:
        if n % 2 == 0:
            return power(a ** 2, n / 2)
        else:
            return a * (power(a, n - 1))


