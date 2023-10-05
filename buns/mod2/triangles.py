sides = input().split(sep=' ')

for i in range (3):
    sides[i] = int(sides[i])


if sides[0] == sides [1] == sides[2]:
    print('Можно построить треугольник')
    print('Равносторонний')
elif sides[0] < sides[1] + sides[2] or sides[1] < sides[0] + sides[2] or sides[2] < sides[1] + sides[0]:
    print('Можно построить треугольник')
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        print('Равнобедренный')