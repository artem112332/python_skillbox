numbers = input().split(sep=' ')
result = True if len(set(numbers)) == len(numbers) else False
print(result)
