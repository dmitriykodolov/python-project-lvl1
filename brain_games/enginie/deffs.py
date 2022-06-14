import prompt
import random


def hello():  # функция приветствие на экран
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")  # запрос имени
    print(f'Hello, {name}')
    return name


def answers():
    answer = prompt.string('Your answer ').lower()  # ответ пользователя
    return answer


def maths():  # переменные для calc и even
    num1, num2 = random.randint(1, 10), random.randint(1, 11)
    # переменные строк и вычислений
    plus, plus_str = num1 + num2, str(f'{num1}+{num2}')
    minus, minus_str = num1 - num2, str(f'{num1}-{num2}')
    multiply, multiply_str = num1 * num2, str(f'{num1}*{num2}')

    # создание случайных арифметических примеров
    random_operation = random.choice([plus, minus, multiply])

    # создаем строку примера
    if random_operation == plus:
        random_operation_str = plus_str
    elif random_operation == minus:
        random_operation_str = minus_str
    else:
        random_operation_str = multiply_str
    return random_operation, random_operation_str, num1


def nums1():
    # генерируем псевдослучайные числа
    x, y = random.randint(1, 100), random.randint(1, 100)
    return x, y
