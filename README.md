# result_store_exercise_decorators
Create a class called store_results. It should be used as a decorator and store information about the executed functions in a file called results.txt in the format: "Function {func_name} was add called. Result: {func_result}"
Test Code
@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)

results.txt
Function 'add' was called. Result: 4
Function 'mult' was called. Result: 24
