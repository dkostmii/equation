# Equation

Python project to evaluate and calculate simple linear equation

## Output

```Python
def main():
  print("Evaluating statements")
  print(evalEq("120 * x - 32,26"))
  print(evalEq("120x - 32,26"))
  print(evalEq("120*x + 32,26"))
  print()

  print("Solving equation")
  print(evalEq("2x - 4").calc(0))


# Output:

# Evaluating statements
# f(x) = 120.0 * x - 32.26   
# f(x) = 120.0 * x - 32.26   
# f(x) = 120.0 * x + 32.26   

# Solving equation
# f(0) = 2.0 * 0 - 4.0 = -4.0
# -4.0
```
