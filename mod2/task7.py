string = input()
string += ' '

count_of_0 = 0
count_of_1 = 0

char = 0
while True:
    if string[char] == ' ':
        break
    else:
        if string[char] == '1':
            count_of_1 += 1
        else:
            count_of_0 += 1
        char += 1

if count_of_0 == count_of_1:
    print('yes')
else:
    print('no')
