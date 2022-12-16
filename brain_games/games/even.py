from random import randint
from brain_games.cli import welcome_user
from brain_games.logic import compare, correct, wrong_answer

def even_start():
    name = welcome_user()
    print("Answer 'yes' if number is even, otherwise answer 'no'")
    count_correct_answers = 0
    return (result(name, count_correct_answers))


def operation():
    number = randint(1, 100)
    print(f"Question: {number}")
    answer = input("Your answer: ").lower()
    
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    
    return (compare(answer, correct_answer))
        

def result(name, count_correct_answers):
    compare, correct_answer, answer = operation()
    if compare:
        tmp = correct(name, count_correct_answers)
        try:
            result(name, tmp)
        except:
            print(tmp)
            
    else:
        return (wrong_answer(answer, correct_answer, name))
