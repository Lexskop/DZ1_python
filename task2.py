# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# # Нужно написать таблицу истинности.

print('Приветствую! Эта программа проверет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат и напишет таблицу истинности.')
print('X,Y,Z -> Ответ')
print('--------------')
approvals = [0,0,0]
for approvals[0] in range(0,2):
    for approvals[1] in range(0,2):
        for approvals[2] in range(0,2):
            print(f'{approvals[0]},{approvals[1]},{approvals[2]} ->',bool(bool(not(approvals[0] or approvals[1] or approvals[2])) == bool(not approvals[0] and not approvals[1] and not approvals[2])))