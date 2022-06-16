from brain_games.enginie.deffs import hello, maths, prompt


def quiz_calc():
    name = hello()
    for answer in range(3):
        random_operation, random_operation_str, num1 = maths()
        print(f'Question: {random_operation_str}')
        answer = prompt.string('Your answer: ').lower()

        if str(random_operation) == answer:
            print('Сorrect!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{random_operation}\'. ''\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
