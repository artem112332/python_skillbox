summ = 0
count = 0
while True:
    n = int(input())
    if n != 0:
        summ += n
        count += 1
    else:
        break

print(summ / count)
    