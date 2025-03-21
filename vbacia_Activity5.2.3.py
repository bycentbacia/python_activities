

expressions = [
    
    "5 + 2 * 3",
    "(5 + 3) * 2",
    "10 - 4 / 2 + 6",
    "2 ** 3  * 4",
    "(10 % 3 ) + (2 ** 3) - 1"
]

# evaluate and print the result
for expr in expressions:
    result = eval(expr) 
    print(f"{expr} = {result}")
     