__author__ = 'Vincent'

import sys
import inspect
import traceback

#include autograder tests here. These should not need to be modified
#DO NOT INCLUDE exception testing here. Those should be addressed in autograder.py

def basic(inputs, correct_function, student_function):
    #The goal of the basic autograder is to run a battery of tests to see if the correct output is returned
    output_correct = []
    output_student = []

    for input in inputs:
        output_correct.append(correct_function(*input))
        output_student.append(student_function(*input))

    i = 0
    incorrect = []
    while i < len(output_correct):
        if output_correct[i] != output_student[i]:
            incorrect += inputs[i]
        i+=1

    return incorrect

### You may add more sophisticated unit tests here ###

def output_type(inputs, correct_function, student_function):
    return type(correct_function(*inputs[0]) == student_function(*inputs[0]))

def output_unmodified(inputs, student_function):
    return inputs[0] == student_function(*inputs[0])

### After adding more unit tests, modify the run() function below ###
# Simply add elif cases calling the unit tests in the second if-else block

def run(inputs, correct_function, student_function):
    incorrect = basic(inputs, correct_function, student_function)
    if len(incorrect) == 0:
        f = open('output.txt', 'w')
        f.write("All test cases passed.")
        return True
    else:
        f = open('output.txt', 'w')
        f.write("Test cases failed:\n")
        for case in incorrect:
            f.write(case+"\n")
        f.write("\n")


    if not output_type(inputs, correct_function, student_function):
        f = open('output.txt', 'w')
        f.write("Test cases failed. Student outputs wrong variable type")
        return False
    elif output_unmodified(inputs, student_function):
        f = open('output.txt', 'w')
        f.write("Test cases failed. Student returns unmodified input")
        return False
    else:
        f = open('output.txt', 'w')
        f.write("Test cases failed. Error found in student code.")
        return False
    return False