# Завдання 1
# У списку цілих, заповненому випадковими числами обчислити:
# - Суму негативних чисел;
# - Суму парних чисел;
# - Суму непарних чисел;
# - Добуток елементів з кратними індексами 3;
# - Добуток елементів між мінімальним та максимальним елементом;
# - Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# Завдання 2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# - Створити список цілих, що містить лише парні числа з першого списку;
# - Створити список цілих, що містить лише непарні числа з першого списку;
# - Створити список цілих, що містить лише негативні числа з першого списку;
# - Створити список цілих, що містить лише позитивні числа з першого списку.

####### Завдання 1

import random

NUMS_SIZE = 20
MIN_NUMBER = -10
MAX_NUMBER = 10

random_numbers = []

try:
    for _ in range(NUMS_SIZE):
        random_numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
    #
    # Суму негативних чисел
    negative_sum = sum(num for num in random_numbers if num < 0)

    # Суму парних чисел
    even_sum = sum(num for num in random_numbers if num % 2 == 0)

    # Суму непарних чисел;
    odd_sum = sum(num for num in random_numbers if num % 2 != 0)

    # Добуток елементів з кратними індексами 3;
    product_indices_3 = 1
    for i in range(0, len(random_numbers), 3):
        product_indices_3 *= random_numbers[1]

    # Добуток елементів між мінімальним та максимальним елементом
    min_index = random_numbers.index(min(random_numbers))
    max_index = random_numbers.index(max(random_numbers))
    if min_index < max_index:
        product_min_max = 1
        for i in range(min_index + 1, max_index):
            product_min_max *= random_numbers[1]
    else:
        product_min_max = 1

    # Суму елементів, що знаходяться між першим та останнім позитивними елементами

    first_positive_num_index, last_positive_num_index = 0, 0

    for i in range(len(random_numbers)):
        if random_numbers[i] > 0:
            first_positive_num_index = i
            break

    for i in range(len(random_numbers) - 1, -1, -1):
        if random_numbers[i] > 0:
            first_positive_num_index = i
            break

    if first_positive_num_index > last_positive_num_index:
        first_positive_num_index, last_positive_num_index = last_positive_num_index, first_positive_num_index

        numbers_range_sum = 0

        for i in range(first_positive_num_index + 1, last_positive_num_index):
            numbers_range_sum += random_numbers[i]

    print("Список цілих чисел:", random_numbers)
    print("Сума негативних чисел:", negative_sum)
    print("Сума парних чисел:", even_sum)
    print("Сума непарних чисел:", odd_sum)
    print("Добуток елементів з кратними індексами 3:", product_indices_3)
    print("Добуток елементів між мінімальним та максимальним елементом:", product_min_max)
    print("Сума елементів між першим та останнім позитивними елементами:", numbers_range_sum)

except Exception as e:
    print(f"Виникла помилка: {e}")