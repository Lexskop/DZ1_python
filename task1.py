# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def user_another_try():
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N -> ')
    if user_choice.lower() == 'y':
        calc()
    else:
        print('Bye!')

def calc():
    day_of_week = input('Введите число, соответствующее дню недели -> ')
    while day_of_week.isdigit() == False:
        print('Вы ошиблись и ввели "не число"')
        day_of_week = input('Введите число, соответствующее дню недели -> ')
    day_of_week = int(day_of_week)
    if bool(day_of_week in range(1, 6)) == True:
        print('Этот день недели не является выходным')
    elif bool(day_of_week in range(6, 8)) == True:
        print('Этот день недели является выходным')
    else:
        print('Введите правильное число дня недели')
    user_another_try()

print('Приветствую! Эта программа покажет, является ли выходным днем недели введенное Вами число, которое должно соответствовать дню недели!')
calc()