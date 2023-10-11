string = input()
result = 'yes' if len(''.join(string.split(sep='0'))) == len(string) / 2 else 'no'
print(result)
