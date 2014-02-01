__author__ = 'Vincent'

import sys
import code
import test_correct
import tests

#Input the name of the function here.
function = code.abbreviate_name
correct = test_correct.abbreviate_name

#Input input parameters for the function here. If the function takes multiple input parameters, put them in lists
#For example: inputs = [(1,2,3), (4,5,6), (7,8,9)]
inputs = ["Sarah Lyons", "John Henry Eden", "Alistair Tenpenny", "Three Dog", "Colin Moriarty", "Lucas Simms",
          "Moira Brown", "The Lone Wonderer", "Abraham Washington", "Amata Almodover", "Crazy Wolfgang"
          "One Two-Three Four", "One-Two Three-Four Five-Six", "One",]

try:
    function(inputs[0])
except:
    sys.exit("Error! Function not found in code. Shutting down autograder.")


