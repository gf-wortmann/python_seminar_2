# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import math
import input_check as IC

def answerOut(count:int):
    print(f'Count of coins to be reversed is {count}')
  
coinsCount = int(IC.IntCheckedInput('Enter count of coins: '))
headsCount = 0
tailsCount = 0

for i in range ( coinsCount ) :
    u = IC.OneOrZero('If you see a head on the coin enter "1" else enter "0" for a tail.')
    if int(u) == 1:
        headsCount+=1
    elif int(u) == 0:
        tailsCount+=1

if headsCount > tailsCount:
    answerOut(tailsCount)
elif tailsCount > headsCount:
    answerOut(headsCount)