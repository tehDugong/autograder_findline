__author__ = 'Vincent'

import sys
import test_correct
import traceback

try:
    import code
except SyntaxError:
    sys.exit("Error! There is a syntax error in the student's code")
except:
    sys.exit("Error! Student code failed to import")

try:
    import tests
except SyntaxError:
    sys.exit("Error! tests.py has a syntax error in it.")
except:
    sys.exit("Error! Failed to import autograder tests. Are you sure tests.py is configured properly?")

###Begin configuring code here. DO NOT MODIFY CODE ABOVE THIS LINE###

#Input the name of the function here.
#Unless students are given instructions to name their files a specific way, there's no way to skip this step
    #Thanks to Soumya Basu for help resolving this issue
#For example : function = code.foobar
#              correct = test_correct.abbreviate_name
function = code.abbreviate_name
correct = test_correct.abbreviate_name

#Input input parameters for the function here. All inputs should be in arrays.
#For example: inputs = [[1,2,3], [4,5,6], [7,8,9]]
inputs = [["Sarah Lyons"], ["John Henry Eden"], ["Alistair Tenpenny"], ["Three Dog"], ["Colin Moriarty"],
          ["Moira Brown"], ["The Lone Wanderer"], ["Abraham Washington"], ["Amata Almodover"], ["Crazy Wolfgang"],
          ["One Two-Three Four"], ["One-Two Three-Four Five-Six"], ["One"]]


###DO NOT MODIFY CODE BELOW THIS LINE###

#All problems that cause exceptions should be addressed here
try:
    function(*inputs[0])
except SyntaxError as e:
    s = traceback.format_exc(e)
    f = open('output.txt', 'w')
    f.write(s)
    sys.exit("Student code has a Syntax Error. Shutting down autograder")
except TypeError as e:
    s = traceback.format_exc(e)
    f = open('output.txt', 'w')
    f.write(s)
    sys.exit("Student code has incorrect number of input parameters. Shutting down autograder")
except AttributeError as e:
    s = traceback.format_exc(e)
    f = open('output.txt', 'w')
    f.write(s)
    sys.exit("Function not found in code. Shutting down autograder.")
except Exception as e:
    s = traceback.format_exc(e)
    f = open('output.txt', 'w')
    f.write(s)
    sys.exit("There is an error in the student's code that causes a crash. Shutting down autograder")

#Battery of tests here.
#If all outputs are correct, then the code is considered to be 100% correct
tests.run(inputs, correct, function)
print("Code successfully tested. Check output.txt for details.")