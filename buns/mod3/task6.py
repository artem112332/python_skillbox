words = input().split(sep=' ')
result = ''.join([words[i][-1] for i in range(len(words))])
print(result)
