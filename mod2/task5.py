string = input()
string += ' '

i = string[0]
n = ''

char = 2

while True:
    if string[char] == ' ':
        n = int(n)
        break
    else:
        n += string[char]
        char += 1

print(chr(97 + ((ord(i) - 97) + n) % 26))
