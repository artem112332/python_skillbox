string = input()
i = string[-1]
s = string[:-2]
count_of_i = 0

char = 0
while True:
    if string[char] == i:
        count_of_i += 1
        char += 1
    else:
        break

print(count_of_i)
