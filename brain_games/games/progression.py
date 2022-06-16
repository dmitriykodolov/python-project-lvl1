import random
from brain_games.enginie.deffs import hello, prompt


def progression():
    def prog_math():
        # список рандомных чисел для работы
        list_prog = []

        random_index = random.randrange(10, 56, 3)
        # переменная для плавающих точек по списку
        index_change = random.randint(1, 9)

        # генерация случайной последовательности
        x = random.randint(12, 56)
        # генерация разности арифсети
        d = random.randint(1, 5)

        # добавляем последовательность в список
        while len(list_prog) < random_index:
            x += d
            list_prog.append(x)

        # отрезаем все после 10 строк
        del list_prog[10:]

        # переменная с правильным ответом
        correct = str(list_prog[index_change])

        # добавляем точки в случайном порядке
        for i in str(list_prog):
            list_prog[index_change] = '..'
            i += i

        operate_string = ' '.join(map(str, list_prog))

        return operate_string, correct

    name = hello()
    print("What number is missing in the progression?")

    for answer in range(3):
        operate_string, correct = prog_math()
        question = f'Question: {operate_string}'
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct}. ''\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
