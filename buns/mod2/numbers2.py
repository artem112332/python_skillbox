summ = 0
count_of_numbers = 0
count_of_zeros = 0
while True:
    n = int(input())
    if n != 0:
        summ += n
        count_of_numbers += 1
    elif n == 0 and count_of_zeros != 2:
        count_of_zeros += 1
    else:
        break

print(summ / count_of_numbers)
