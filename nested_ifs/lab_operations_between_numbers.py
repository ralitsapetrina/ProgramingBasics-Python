n1 = int(input())
n2 = int(input())
operator = input()

add = "+"
subtr = "-"
mult = "*"
divide = "/"
module = "%"

result = None

if operator == add:
    result = n1 + n2
elif operator == subtr:
    result = n1 - n2
elif operator == mult:
    result = n1 * n2
elif operator == divide:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
elif operator == module:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2

even_odd = ""
if result:
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

if operator == add or operator == subtr or operator == mult:
    print(f"{n1} {operator} {n2} = {result} - {even_odd}")
elif operator == divide:
    if result:
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == module:
    if result:
        print(f"{n1} % {n2} = {result}")