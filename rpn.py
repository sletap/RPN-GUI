#!/usr/bin/env python3
import sys
import readline 
from math import factorial
from math import sqrt
import decimal
import operator
import GUI

def calculate(arg):
  stack = []

  tokens = arg.split()
  # print(tokens)
  for token in tokens:
    try:
      stack.append(float(token))
    except ValueError:
      if len(stack) > 0:
        val2 = stack.pop()
      if len(stack) > 0:
        val1 = stack.pop()
      if token == '+':
        result = val1 + val2
      elif token == '-':
        result = val1 - val2
      elif token == '*': #need to add test
        result = val1 * val2
      elif token == '^': #exponent
        result = val1**val2
      elif token == '/': #exponent
        result = val1/val2
        result = format(result, ".2f")
      elif token == '!': #factorial
        result = factorial(val2)
      elif token == '&': #and
        result = val1 & val2
      elif token == '|': #or
        result = val1 | val2
      elif token == '~': #not
        result = ~val2
      elif token == "ptC":
        result = sqrt(val1*val1 + val2*val2)
      elif token == "ptA":
        result = sqrt(abs(val1*val1 - val2*val2))
      elif token == "ptB":
        result = sqrt(abs(val1*val1 - val2*val2))
      stack.append(result)


      if len(stack) > 1:
        raise ValueError('Too many arguments on the stack')

      return stack[0];

def startGUI():
  print("Starting GUI")
  app = GUI.QApplication(sys.argv)
  calculator = GUI.RPNGUI()
  calculator.show()
  sys.exit(app.exec_())

def main():
  while True:
    try:
      inp = input("rpn calc> ")
      if inp == "GUI":
        startGUI()
      else:
        result = calculate(inp)
        print(result)
    except ValueError:
      pass


if __name__ == '__main__':
  main();
