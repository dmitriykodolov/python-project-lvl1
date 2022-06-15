from brain_games.enginie.deffs import hello, prompt
import random


def prime_num(x):
    # if num is 0 or 1 there are not
    # prime or composite nums
    if x == 0 or x == 1:
        print('Not prime & not composite num')
    else:
        # every number can be
        # divisible by itself or one.
        # Range not include 1 or number
        for i in range(2, x):
            # if num is composite, it should have
            # at least one divine
            if x % i == 0:
                # composite num return False
                return False
        else:
            # prime num return True
            return True
    return True, False


def prime_game():
    name = hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for answer in range(3):
        num1 = random.randint(2, 100)

        print(f'Question: {num1}')

        if prime_num(num1) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = prompt.string('Your answer ').lower()

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}". '
                  f'Let\'s try again, {name}')
            break
    else:
        print(f'Congratulations, {name}!')
