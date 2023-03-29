# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

from input_check import IntCheckedInput, IntCheckedInputLtd


thinkedSum = int(IntCheckedInputLtd('Enter the sum of numbers', 2001))
thinkedProd = int(IntCheckedInputLtd('Enter the product of numbers', 1000001    ))
found = False
for numberOne in range (thinkedSum):
    if not found:
        for numberTwo in range (thinkedProd):
            if not found:
                if numberOne+numberTwo == thinkedSum and numberOne*numberTwo == thinkedProd:
                    print (f'Number one = {numberOne} and number two = {numberTwo}')
                    found = True
if not found:
    print('It seems there is no decision..')
