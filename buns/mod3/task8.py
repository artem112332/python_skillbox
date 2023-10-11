string = input()
result = string.translate({ord(c): None for c in ' ()-'})
print(result)
