# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.

from input_check import IntCheckedInputLtd

limit = 1000000
ceiling = IntCheckedInputLtd(f'Enter natural number less, than {limit}', limit)
i = 0
while 2 ** i <= ceiling:
    print (f' 2^{i} = {2 ** i}')
    i += 1