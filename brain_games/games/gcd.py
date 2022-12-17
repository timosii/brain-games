from random import randint
from brain_games.cli import welcome_user
from brain_games.logic import compare, correct, wrong_answer


def gcd_start():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    count_correct_answers = 0
    return (result(name, count_correct_answers))


def operation():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print(f"Question:{number1} {number2}")
    answer = input("Your answer: ")
    list_numbers = sorted([number1, number2])
    num_min, num_max = list_numbers[0], list_numbers[1]
    list_dividers = []
    for num in range(1, num_min + 1):
        if (num_min % num == 0) and (num_max % num == 0):
            list_dividers.append(num)
    correct_answer = str(max(list_dividers))
    return (compare(answer, correct_answer))


def result(name, count_correct_answers):
    compare, correct_answer, answer = operation()
    if compare:
        tmp = correct(name, count_correct_answers)
        try:
            result(name, tmp)
        except Exception:
            print(tmp)
    else:
        return (wrong_answer(answer, correct_answer, name))
