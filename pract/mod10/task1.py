import re
import doctest


def check_password(password: str):
    """
    >>> check_password('rtG3FG!Tr^e')
    True
    >>> check_password('aA1!*!1Aa')
    True
    >>> check_password('oF^a1D@y5e6')
    True
    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$$W0Rd')
    False
    """
    conditions = []
    pattern_1 = r'[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789^$%@#&*!?]+'
    pattern_2 = r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+'
    pattern_3 = r'[0123456789]'
    pattern_4 = r'[/^$%@#&*!?]'
    pattern_5 = r'((.)\2{2,})'
    conditions.append(''.join(re.findall(pattern_1, password)) == password)
    conditions.append(len(password) >= 6)
    conditions.append(len(''.join(re.findall(pattern_2, password))) >= 2)
    conditions.append(len(re.findall(pattern_3, password)) >= 1)
    conditions.append(len(''.join(set((re.findall(pattern_4, password))))) >= 2)
    conditions.append(len(re.findall(pattern_5, password)) == 0)

    for _ in range(len(conditions)):
        if not conditions[_]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
