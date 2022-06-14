from brain_games.enginie.deffs import prompt, hello, nums1


def euclidian():
    name = hello()
    print("Find the greatest common divisor of given numbers.")
    for answer in range(3):
        x, y = nums1()
        print(f'Question: {x} {y}')
        answer = prompt.string("Your answer: ")
        while y > 0:
            x, y = y, x % y
        correct_answer = str(x)
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f'\'{answer}\' is wrong answer ;(. ''\n'
                  f'Correct answer was \'{correct_answer}\'.''\n'
                  f'Let\'s try again, {name}')
            break
    else:
        print(f'Congratulations, {name}!')
