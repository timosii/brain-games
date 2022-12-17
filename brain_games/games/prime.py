from random import randint
from brain_games.cli import welcome_user
from brain_games.logic import compare, correct, wrong_answer


def prime_start():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_correct_answers = 0
    return (result(name, count_correct_answers))


def operation():
    number = randint(1, 100)
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if number in prime_numbers:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    print(f"Question: {number}")
    answer = input("Your answer: ").lower()
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
