string = input()

isPalindrom = True

for i in range(len(string)):
    if string[i] == string[len(string)-1-i]:
        continue
    else:
        isPalindrom = False
        break

if isPalindrom:
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')