def convert_to(n, base):
    digits = '0123456789abcdef'
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result


string = input('Введите натуральное число: ')

number = 0

# проверка на натуральное число
if float(string) < 0 or float(string) % 1 > 0:
    print('Неверный ввод')
else:
    number = int(string)

binary_number = convert_to(number, 2)
octal_number = convert_to(number, 8)
hexadecimal_number = convert_to(number, 16)

print(f'{binary_number}, {octal_number}, {hexadecimal_number}')


