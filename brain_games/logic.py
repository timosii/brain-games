def compare(answer, correct_answer):
    if answer == correct_answer:
        compare = True
    else:
        compare = False

    return compare, correct_answer, answer


def correct(name, count_correct_answers):
    print("Correct!")
    if count_correct_answers < 1:
        count_correct_answers += 1
        return count_correct_answers
    else:
        return (f'Congratulations, {name}!')


def wrong_answer(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
