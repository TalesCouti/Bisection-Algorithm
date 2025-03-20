import math
# Initial guesses
a = 0.1 
b = 5 
i = 1 
x = (a + b) / 2 

function = x**2 + math.log(x)  # Function 
print(f'Iteration {i}:')
print(f'  x = {x}')
print(f'  a = {a}')
print(f'  b = {b}')
print(f'  function = {function}')
print('-----------------------')

while b - a > 0.01:  # Precision
    if function > 0:
        b = x
    else:
        a = x

    x = (a + b) / 2
    function = x**2 + math.log(x)

    i += 1
    print(f'Iteration {i}:')
    print(f'  x = {x}')
    print(f'  a = {a}')
    print(f'  b = {b}')
    print(f'  function = {function}')
    print('-----------------------')

print(f'Approximate root found: {x}')
print(f'Function value at the root: {function}')
print(f'Number of iterations: {i}')
