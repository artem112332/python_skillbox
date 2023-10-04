string = input('Введите 3 числа, разделённые пробелом: ')
string += ' '

# преобразование строки в 3 числа
num1 = ''
num2 = ''
num3 = ''

digit = 0
while True:
    if string[digit] == ' ':
        num1 = int(num1)
        break
    else:
        num1 += string[digit]
        digit += 1

digit += 1
while True:
    if string[digit] == ' ':
        num2 = int(num2)
        break
    else:
        num2 += string[digit]
        digit += 1


digit += 1
while True:
    if string[digit] == ' ':
        num3 = int(num3)
        break
    else:
        num3 += string[digit]
        digit += 1

minimum = 0
middle = 0
maximum = 0

# сортировка
if num1 > num2 and num1 > num3:
    maximum = num1
    if num2 > num3:
        middle = num2
        minimum = num3
    else:
        middle = num3
        minimum = num2
elif num2 > num1 and num2 > num3:
    maximum = num2
    if num1 > num3:
        middle = num1
        minimum = num3
    else:
        middle = num3
        minimum = num1
else:
    maximum = num3
    if num1 > num2:
        middle = num1
        minimum = num2
    else:
        middle = num2
        minimum = num1

print(middle)
