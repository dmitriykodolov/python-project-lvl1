from brain_games.enginie.deffs import maths, hello, prompt


def quiz_even():
    name = hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for answer in range(3):
        question = maths()[2]
        print(f'Question: {question}')
        answer = prompt.string('Your answer ').lower()
        if question % 2 == 0 and answer == 'yes' \
                or question % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            if question % 2 != 0 and answer == 'yes':
                print(f'{answer} is wrong answer ;(. '
                      f'Correct answer was \'no\'. Let\'s try again, {name}!')
                break
            elif question % 2 == 0 and answer == 'no':
                print(f'{answer} is wrong answer ;(. '
                      f'Correct answer was \'yes\'. Let\'s try again, {name}!')
                break

    else:
        print(f'Congratulations, {name}!')
