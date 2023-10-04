string = input()
string += ' .'
word = ''

char = 0
while string[char] != '.':
    if string[char] == ' ':
        word += string[char-1]
        char += 1
    else:
        char += 1

print(word)
