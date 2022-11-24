# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)

def choice_quarter():
    quarter = input('Введите номер четверти -> ')
    if quarter.lower() == 'x':
        print('Bye!')
        return
    while quarter.isdigit() == False or bool(int(quarter) in range(1, 5)) == False:
        print('Вы ошиблись и неверно ввели номер четверти! Попробуйте еще раз!')
        quarter = input('Введите номер четверти -> ')
        if quarter.lower() == 'x':
            print('Bye!')
            return
    quarter = int(quarter)
    if quarter == 1:
        print('При','\033[34m {}'.format('первом'),'\033[0m {}'.format('номере четверти диапазон возможных координат точек будет'),'\033[34m {}'.format('x∈(0, ∞) u y∈(0, ∞)'),'\033[0m {}'.format(''))
    if quarter == 2:
        print('При','\033[34m {}'.format('втором'),'\033[0m {}'.format('номере четверти диапазон возможных координат точек будет'),'\033[34m {}'.format('x∈(-∞, 0) u y∈(0, ∞)'),'\033[0m {}'.format(''))
    if quarter == 3:
        print('При','\033[34m {}'.format('третьем'),'\033[0m {}'.format('номере четверти диапазон возможных координат точек будет'),'\033[34m {}'.format('x∈(-∞, 0) u y∈(-∞, 0)'),'\033[0m {}'.format(''))
    if quarter == 4:
        print('При','\033[34m {}'.format('четвёртом'),'\033[0m {}'.format('номере четверти диапазон возможных координат точек будет'),'\033[34m {}'.format('x∈(0, ∞) u y∈(-∞, 0)'),'\033[0m {}'.format(''))
    user_another_try()

def user_another_try():
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n' and user_choice.lower() != 'x':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N или X -> ')
    if user_choice.lower() == 'y':
        choice_quarter()
    else:
        print('Bye!')

print('Приветствую! Эта программа по заданному номеру четверти покажет диапазон возможных координат точек в этой четверти (x и y). Для выхода из программы -> введите X!')
choice_quarter()