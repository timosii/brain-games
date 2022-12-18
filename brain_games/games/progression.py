from random import randint
from brain_games.cli import welcome_user
from brain_games.logic import compare, correct, wrong_answer


def progression_start():
    name = welcome_user()
    print("What number is missing in the progression?")
    count_correct_answers = 0
    return (result(name, count_correct_answers))


def operation():
    len_progression = randint(5, 10)
    start = randint(1, 50)
    step = randint(1, 10)
    finish = start + step * len_progression + 1
    progression = list(range(start, finish + step, step))
    index_progression = randint(0, len(progression) - 1)
    progression[index_progression] = '..'
    progression = ' '.join(map(str, progression))
    progression_correct = list(range(start, finish + step, step))
    print(f"Question: {progression}")
    answer = input("Your answer: ")
    correct_answer = str(progression_correct[index_progression])
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
