from random import randint, choice
from brain_games.cli import welcome_user


def calc():
    name = welcome_user()
    print("What is the result of the expression?")
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
    number1 = randint(1, 35)
    number2 = randint(1, 35)
    list_oper = ["*", "-", "+"]
    operation = choice(list_oper)
    print(f"Question: {number1} {operation} {number2}")
    answer = input("Your answer: ")
    result = eval(f"{number1}{operation}{number2}")
    if str(answer) == str(result):
        return True
    else:
        return (f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
