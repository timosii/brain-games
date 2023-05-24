from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.common_part import compare, correct, wrong_answer


def calc_start():
    name = welcome_user()
    print("What is the result of the expression?")
    count_correct_answers = 0
    return (result(name, count_correct_answers))


def operation():
    number1 = randint(1, 35)
    number2 = randint(1, 35)
    list_oper = ["*", "-", "+"]
    selection = choice(list_oper)
    print(f"Question: {number1} {selection} {number2}")
    answer = input("Your answer: ")
    correct_answer = str(eval(f"{number1}{selection}{number2}"))
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
