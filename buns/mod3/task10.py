size = int(input())
matrix = []

for i in range(size):
    matrix.append(list())

for a in range(size):
    for b in range(size):
        if b != size - 1:
            print(b + 1, end=', ')
        else:
            print(b + 1)

print('')

for a in range(size):
    for b in range(size):
        if b != size - 1:
            print(a + 1, end=', ')
        else:
            print(a + 1)
