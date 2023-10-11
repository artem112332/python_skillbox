str1 = input()
str2 = input()
str3 = input()

winnerFound = False
for c in 'XO':
    if set(str1) == c or set(str2) == c or set(str3) == c:
        print(c)
        winnerFound = True
        break

    for i in range(3):
        if str1[i] == str2[i] == str3[i] == c:
            print(c)
            winnerFound = True
            break

    if str1[0] == str2[1] == str3[2] == c:
        print(c)
        winnerFound = True
        break

    if str1[2] == str2[1] == str3[0] == c:
        print(c)
        winnerFound = True
        break

if not winnerFound:
    print('Ничья')




