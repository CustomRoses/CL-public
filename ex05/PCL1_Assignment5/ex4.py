def function1():
    sentence = "I love you!"
    print(sentence)
    # The variable sentence that is defined in this function is local to the scope of the function, and is therefore not defined in the global scope.


sentence = "I miss you!"
# set the variable 'sentence' in the global scope to 'I miss you!'
function1()
# call the function 'function1', which only modifies the local variable 'sentence'. this has no effect on the global variable 'sentence'

print(sentence)
# we can print the global variable 'sentence' to see that it has not been modified by the function 'function1'
