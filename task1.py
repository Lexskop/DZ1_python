# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def calc():
    user_number = input('Введите число, соответствующее дню недели -> ')
    if user_number.lower() == 'x':
        print('Bye!')
        return
    while user_number.isdigit() == False or bool(int(user_number) in range(1, 8)) == False:
        if user_number.isdigit() == False:
            print('Вы ошиблись и ввели "не число"!')
        if user_number.isdigit() == True and bool(int(user_number) in range(1, 8)) == False:
            print('Вы ввели число, не соответствующее дню недели!')
        user_number = input('Введите число, соответствующее дню недели -> ')
        if user_number.lower() == 'x':
            print('Bye!')
            return
    user_number = int(user_number)
    days_of_the_week = ['Понедельник!','Вторник!','Среда!','Четверг!','Пятница!','Суббота!','Воскресенье!']
    if bool(user_number in range(1, 6)) == True:
        print('Выбранный день недели ->','\033[33m {}'.format(days_of_the_week[user_number-1]),'\033[0m {}'.format('Этот день недели'),'\033[31m {}'.format('не является'),'\033[0m {}'.format('выходным!'))
    elif bool(user_number in range(6, 8)) == True:
        print('Ваш день недели ->','\033[33m {}'.format(days_of_the_week[user_number-1]),'\033[0m {}'.format('Этот день недели'),'\033[34m {}'.format('является'),'\033[0m {}'.format('выходным!'))
    user_another_try()

def user_another_try():
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n' and user_choice.lower() != 'x':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N или X -> ')
    if user_choice.lower() == 'y':
        calc()
    else:
        print('Bye!')

print('Приветствую! Эта программа покажет, является ли выходным днем недели введенное Вами число, которое должно соответствовать дню недели! Для выхода из программы - введите X')
calc()