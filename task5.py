# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

def calc():
    coordinates_of_dots = []
    print('Введите координаты точек через пробел X1 Y1 X2 Y2 -> ')
    for i in input().split():
        coordinates_of_dots.append(int(i))
    print('A('f'{coordinates_of_dots[0]},{coordinates_of_dots[1]}) B('f'{coordinates_of_dots[2]},{coordinates_of_dots[3]}) -> ',round(((coordinates_of_dots[2]-coordinates_of_dots[0])**2 + (coordinates_of_dots[3]-coordinates_of_dots[1])**2)**(1/2),3))
    user_another_try()


def user_another_try():
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N -> ')
    if user_choice.lower() == 'y':
        calc()
    else:
        print('Bye!')

print('Приветствую! Эта программа принимает на вход координаты двух точек A(X1,Y1) и B(X2,Y2) и находит расстояние между ними в 2D пространстве!')
calc()