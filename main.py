import random

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
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        if guess == str(answer):
            print("Correct!")
            break
        else:
            print("Try again.")