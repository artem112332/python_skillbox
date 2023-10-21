def analyze(numbers_list):
    if len(numbers_list) == len(set(numbers_list)):
        print('Все числа разные')
    elif len(set(numbers_list)) == 1:
        print('Все числа равны')
    else:
        print('Есть равные и неравные числа')
