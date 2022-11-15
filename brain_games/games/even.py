from random import randint
from brain_games.cli import welcome_user


def even():
    name = welcome_user()
    print("Answer 'yes' if number is even, otherwise answer 'no'")
    result = correct(name)
    print(result)


def correct(name):
    count_correct_answers = 0
    while count_correct_answers < 3:
        res = correct_answer(name)
        if res is True:
            count_correct_answers += 1
            print("Correct!")
            if count_correct_answers == 3:
                return (f'Congratulations, {name}!')
        else:
            return res
            break
                     

def correct_answer(name):
    number = randint(1, 100)
    print(f"Question: {number}")
    answer = input("Your answer: ").lower()
    if ((answer == 'yes' and number % 2 == 0) or
            (answer == 'no' and number % 2 != 0)):
        return True
    elif number % 2 == 0:
        return (f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\
                \nLet's try again, {name}!")
    elif number % 2 != 0:
        return (f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\
                \nLet's try again, {name}!")
