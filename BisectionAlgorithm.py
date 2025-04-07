import math
from openpyxl import Workbook

# Function to be analyzed
def f(x):
    return x**2 + math.log(x)

# Create the Excel file and active sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Bisection Results"

# Headers for the spreadsheet
ws.append(["Iteration", "x", "a", "b", "f(a)", "f(b)", "f(x)", "Sign", "Error"])

# Initial parameters
a = 0.0001 
b = 5 
i = 1 

while b - a > 0.01:  # Desired precision
    x = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fx = f(x)
    error = abs(b - a)
    
    # Determining the sign
    if fa * fx < 0:
        sign = "Negative"
        b = x
    else:
        sign = "Positive"
        a = x

    # Add the current row to the spreadsheet
    ws.append([i, x, a, b, fa, fb, fx, sign, error])

    i += 1

# Save the Excel file
wb.save("bisection_results.xlsx")
print(f"File 'bisection_results.xlsx' saved successfully.")

