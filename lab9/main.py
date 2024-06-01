import random

# Визначаємо розмірність масиву (наприклад, 5x5)
n = 5

# Створюємо двовимірний масив розміром nxn та заповнюємо його випадковими числами
array = []
for i in range(n):
    row = []  # Створюємо новий рядок
    for j in range(n):
        row.append(random.randint(1, 100))  # Додаємо випадкове число до рядка
    array.append(row)  # Додаємо рядок до масиву

# Виводимо згенерований масив
print("Згенерований масив:")
for row in array:
    print(row)

# Ініціалізуємо змінні для зберігання максимальних та мінімальних значень
max_main_diag = -float('inf')  # найменше можливе значення для початку
min_main_diag = float('inf')   # найбільше можливе значення для початку
max_sec_diag = -float('inf')   # найменше можливе значення для початку
min_sec_diag = float('inf')    # найбільше можливе значення для початку

# Проходимо по всім елементам головної та побічної діагоналей
for i in range(n):
    main_diag_value = array[i][i]  # елемент головної діагоналі
    sec_diag_value = array[i][n - i - 1]  # елемент побічної діагоналі

    # Оновлюємо максимальні та мінімальні значення для головної діагоналі
    if main_diag_value > max_main_diag:
        max_main_diag = main_diag_value
    if main_diag_value < min_main_diag:
        min_main_diag = main_diag_value

    # Оновлюємо максимальні та мінімальні значення для побічної діагоналі
    if sec_diag_value > max_sec_diag:
        max_sec_diag = sec_diag_value
    if sec_diag_value < min_sec_diag:
        min_sec_diag = sec_diag_value

# Виводимо результати
print("\nМаксимальне значення головної діагоналі:", max_main_diag)
print("Мінімальне значення головної діагоналі:", min_main_diag)
print("Максимальне значення побічної діагоналі:", max_sec_diag)
print("Мінімальне значення побічної діагоналі:", min_sec_diag)
