#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user


def even():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer 'yes' if number is even, otherwise answer 'no'")
    count_correct_answers = 0
    while count_correct_answers < 3:
        res = correct_answer()
        if res is True:
            count_correct_answers += 1
            print("Correct!")
            if count_correct_answers == 3:
                print(f'Congratulations, {name}!')
        else:
            print(res)
            break


def correct_answer():
    number = randint(1, 100)
    print(f"Question:{number}")
    answer = input().lower()
    if ((answer == 'yes' and number % 2 == 0) or
            (answer == 'no' and number % 2 != 0)):
        return True
    elif number % 2 == 0:
        return (f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\
                \nLet's try again, name!")
    elif number % 2 != 0:
        return (f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\
                \nLet's try again, name!")
