
def store_results(func):
    def wrapper(*args):

        text_in_log = f"Function '{func.__name__}' was add called. Result: {func(*args)}\n"
        with open('results.txt', 'a') as file:
            file.write(text_in_log)
    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

