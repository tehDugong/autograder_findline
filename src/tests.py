__author__ = 'Vincent'

#include autograder tests here
def basic_autograder(inputs, correct_function, student_function):
    #The goal of the basic autograder is to run a battery of tests to see if the correct output is returned
    output_correct = []
    output_student = []
    for input in inputs:
        output_correct += correct_function(input)
        output_student += student_function(input)

    if len(output_correct) != len(output_student):
        return False

    i = 0
    while i < len(output_correct):
        if output_correct[i] != output_student[i]:
            return False
        i+=1
    return True

def run(inputs):
    return