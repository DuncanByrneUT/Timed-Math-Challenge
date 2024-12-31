# importing random and time
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROB = 10
# generating the problem for the user
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

for i in range(TOTAL_PROB):
    expr, answer = generate_problem()
    start_time = time.time() #timer starts
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        if guess == str(answer):
            end_time = time.time() # stops the timer
            time_taken = end_time - start_time
            print(f"Correct! Time Taken: {time_taken} seconds!!")
            break
        else:
            print("Try again.")