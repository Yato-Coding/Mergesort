import numpy as np

# ---Variables---
fib_arr = []
first_number = 0
second_number = 1

def generate_fibonnaci(first_number, second_number, fib_arr):
    for i in range(user_input):
        result = second_number + first_number
        first_number = second_number
        second_number = result
        fib_arr.append(result)
    np.random.shuffle(fib_arr)

user_input = int(input("How many fibonnaci numbers would you like to generate? "))
generate_fibonnaci(first_number, second_number, fib_arr)