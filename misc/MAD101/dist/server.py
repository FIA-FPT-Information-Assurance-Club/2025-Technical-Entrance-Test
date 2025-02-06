#!/usr/local/bin/python
import random
from inputimeout import inputimeout
 
OPERATORS = ['+', '-', '*', '//']

def random_number():
    return str(random.randint(1, 100000))

def random_operator():
    return random.choice(OPERATORS)

def generate_random_formula(max) -> str:
    formula = []
    if max < 3:
        term_count = 3
    else:
        term_count=random.randint(3, max)
    formula.append(random_number())

    for _ in range(term_count - 1):
        formula.append(random_operator())
        formula.append(random_number())

    return ' '.join(formula)

def infix_to_postfix(formula: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '//': 2}
    output = []
    operators = []

    tokens = formula.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return ' '.join(output)

def infix_to_prefix(formula: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '//': 2}
    output = []
    operators = []

    tokens = formula.split()[::-1]

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] > precedence[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return ' '.join(output[::-1])

def make_formula(max):
    formula = generate_random_formula(max)
    try:
        result = eval(formula)
    except ZeroDivisionError:
        result = "Error: Division by zero"
    choice = random.randint(0, 2)
    if choice == 0:
        return formula, result
    elif choice == 1:
        postfix_formula = infix_to_postfix(formula)
        return postfix_formula, result
    elif choice == 2:
        prefix_formula = infix_to_prefix(formula)
        return prefix_formula, result

if __name__ == "__main__":
    print("[+] Welcome to the game")
    print("[+] Answering 1000 questions below will get your flag")
    print("[+] You have 3 seconds for each question. You have casio right?, let it count for you")
    for i in range(1000):
        formula, result = make_formula(i)
        try:
            inp = inputimeout(prompt=formula + " = " , timeout=3)
            if(inp != result):
                print("[-] Nah, see you again!")
                exit()
        except Exception: 
            print("[-] Time limit exceed!")
            exit()
    print("[+] Here is your flag: FIA{https://open.spotify.com/track/6faDaesW1HUcRf7gKKHx7g?si=cac9bb0144cd4683}")