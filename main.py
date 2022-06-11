from typing import Union
from math import isnan
from cmath import isnan
import re

realNumber = Union[int, float]


class MathFunc:
  def __init__(self, a: realNumber, b: realNumber):
    if isnan(a) or isnan(b):
      raise Exception("Both a and b must be a numbers")

    self.a = round(a, 4)
    self.b = round(b, 4)


  # String representation method
  def __repr__(self) -> str:
    if self.a != 0 and self.b != 0:
      if (self.b < 0):
        return f"f(x) = {self.a} * x " + str(self.b).replace("-", "- ")
      else:
        return f"f(x) = {self.a} * x + {self.b}"
    elif self.a != 0:
      return f"f(x) = {self.a} * x"
    else:
      return f"f(x) = {self.b}"


  def calc(self, x: realNumber) -> realNumber:
    value = self.a * x + self.b 
    message = repr(self).replace("x", str(x)) + " = " + str(value)
    print(message)
    return value


  def reverse(self):
    if self.a != 0 and self.b != 0:
      return MathFunc(1 / self.a, -self.b)
    elif self.a != 0:
      return MathFunc(1 / self.a, 0)
    else:
      return MathFunc(0, -self.b)


def evalEq(eq: str) -> MathFunc:
  escaped = re.sub("[^*x\\.\\-+\\d]", "", re.sub(",", ".", eq)).strip()

  if re.match("[*+\\-]{2,}", escaped):
    raise Exception("Invalid statement: " + eq)

  a = float(
      re.sub(
          "\\*|x",
          "", 
          re.sub("(\\+|-)(\\d|\\.)*$".strip(), "", re.sub("\\s", "", escaped)).strip()
        )
    )
  b = float(
      re.sub(
          "\\+", 
          "", 
          re.sub("(\\+|-|)(\\d|\\.)*(\\*|x)", "", re.sub("\\s", "", escaped)).strip()
        )
    )

  return MathFunc(a, b)


def main():
  print("Evaluating statements")
  print(evalEq("120 * x - 32,26"))
  print(evalEq("120x - 32,26"))
  print(evalEq("120*x + 32,26"))
  print()

  print("Solving equation")
  print(evalEq("2x - 4").calc(0))


if __name__ == "__main__":
  main()
