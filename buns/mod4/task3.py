def nod(m, n):
    if n != m:
        if m > n:
            m -= n
        else:
            n -= m
        return nod(m, n)
    else:
        return n


print(nod(451, 287))