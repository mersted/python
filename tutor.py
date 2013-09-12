from math import *
from random import *

def run_code():
    count = 1
    problem_sets(count)

def problem_sets(set_number):

    # Addition
    add = "+"
    answer_a = input("Enter number of addition problems")
    num_probs_a = int(answer_a)

    while num_probs_a < 1:
        print("Not a valid number of problems.")
        answer_a_again = input("Enter number of addition problems")
        num_probs_a = int(answer_a_again)

    c, d = complete_set(add, num_probs_a)

    # Subtraction

    subtract = "-"
    answer_s = input("Enter number of subtraction problems")
    num_probs_s = int(answer_s)

    while num_probs_s < 1:
        print("Not a valid number of problems.")
        answer_s_again = input("Enter number of addition problems")
        num_probs_s = int(answer_s_again)

    e, f = complete_set(subtract, num_probs_s)

    # Multiplication

    multiply = "*"
    answer_m = input("Enter number of multiplication problems")
    num_probs_m = int(answer_m)

    while num_probs_m < 1:
        print("Not a valid number of problems.")
        answer_m_again = input("Enter number of addition problems")
        num_probs_m = int(answer_m_again)

    g, h = complete_set(multiply, num_probs_m)

    correct = c + e + g
    incorrect = d + f + h
    # Adds up correct and incorrect number of problems from each set
    # from the return values of complete_set.

    print_final_results(correct, incorrect, set_number)

    if set_number == 1:
        try_again(set_number)


def complete_set(operator, number):

    a, b = do_one_set(operator, number)
    print_results(a, b)
    return (a, b)


def do_one_set(the_operation, the_problems):

    i = 0
    num_correct = 0
    num_incorrect = 0

    maximum = get_max_num()

    while i < the_problems:

        num_1 = randint(0, maximum)
        num_2 = randint(0, maximum)

        num_1_str = str(num_1)
        num_2_str = str(num_2)

        answer = input(num_1_str + "" + the_operation + "" + num_2_str + "=")
        ans = int(answer)

        i = i + 1

        if the_operation == "+":

            if ans == num_1 + num_2:
                print("Correct")
                num_correct += 1
            else:
                print("Incorrect")
                num_incorrect += 1

        if the_operation == "-":

            if ans == num_1 - num_2:
                print("Correct")
                num_correct += 1
            else:
                print("Incorrect")
                num_incorrect += 1

        if the_operation == "*":

            if ans == num_1 * num_2:
                print("Correct")
                num_correct += 1
            else:
                print("Incorrect")
                num_incorrect += 1

    return (num_correct, num_incorrect)


def get_max_num():

    max_num = input("Enter max number for each problem")

    num_max = int(max_num)

    if num_max < 0:
        print("\nPositive numbers only.")
        get_max_num()

    return num_max


def print_results(correct, incorrect):

    rate = (correct / (correct + incorrect)) * 100
    success_rate_float = float(rate)
    success_rate_str = str("%.2f" % rate)

    print("\nYou got", correct, "problem(s) correct and", incorrect, "incorrect")
    print("for a success rate of", success_rate_str + "%")


def try_again(the_count):

    answer = input("Do you want to do another set?")

    while answer == "yes":
        the_count += 1
        problem_sets(the_count)
        answer = input("Do you want to do another set?")

    if answer == "no":
        print("\nThanks for coming!")


    if answer != "yes" and answer != "no":
        print("\nNot a valid response")



def print_final_results(final_correct, final_incorrect, the_set):

    rate = (final_correct / (final_correct + final_incorrect)) * 100
    rate_float = float(rate)
    rate_str = str("%.2f" % rate_float)

    the_set_str = str(the_set)

    print("\nYou're final results for set", the_set_str + ":")
    print(final_correct, "problems correct and", final_incorrect, "incorrect")
    print("for a success rate of", rate_str + "%")
    
