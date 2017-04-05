#!/usr/bin/env python
# coding: utf-8
"""
A simple text calculator program
It exists for the sole purpose of testing GI
It's not an effective way of doing simple calculations.
"""
import sys
import re
def evaluateString(ter,ops):
    y = str(ter.pop())
    op = ops.pop()
    x = str(float(ter.pop()))
    return eval(x+op+y)

def calculate(in_str):
    operators = []
    numbers = []
    priority = False
    last_i = None
    for i in in_str.strip():
        try:
            dum = round(float(i),2)
            if last_i=='num':
                numbers[-1] += i
            else:
                numbers.append(i)
                last_i = 'num'
        except ValueError:
            if i=="(":
                if len(numbers)>1 and len(operators)>0:
                    y = round(float(numbers.pop()),2)
                    x = round(float(numbers.pop()),2)
                    op = operators.pop()
                    if op == '+':
                        z = x + y
                    elif op == '-':
                        z = x - y
                    elif op == '*':
                        z = x * y
                    elif op == '/':
                        try:
                            z = x / y
                        except ZeroDivisionError:
                            z = 0.0
                    else:
                        z = x
                    numbers.append(z)
                priority = False
            elif not (i=="(" or i==")"):
                if priority and len(numbers)>=1 and len(operators)==0:
                    y = round(float(numbers.pop()),2)
                    x = round(float(numbers.pop()),2)
                    op = operators.pop()
                    if op == '+':
                        z = x + y
                    elif op == '-':
                        z = x - y
                    elif op == '*':
                        z = x * y
                    elif op == '/':
                        try:
                            z = x / y
                        except ZeroDivisionError:
                            z = 0.0
                    else:
                        z = x
                    numbers.append(z)
                if (i=="*") or (i=="/"):
                    priority = True
                elif len(numbers)>1 and len(operators)>0:
                    y = round(float(numbers.pop()),2)
                    x = round(float(numbers.pop()),2)
                    op = operators.pop()
                    if op == '+':
                        z = x + y
                    elif op == '-':
                        z = x - y
                    elif op == '*':
                        z = x * y
                    elif op == '/':
                        try:
                            z = x / y
                        except ZeroDivisionError:
                            z = 0.0
                    else:
                        z = x
                    numbers.append(z)
                operators.append(i)
            elif i==")":
                y = round(float(numbers.pop()),2)
                x = round(float(numbers.pop()),2)
                op = operators.pop()
                if op == '+':
                    z = x + y
                elif op == '-':
                    z = x - y
                elif op == '*':
                    z = x * y
                elif op == '/':
                    try:
                        z = x / y
                    except ZeroDivisionError:
                        z = 0.0
                else:
                    z = x
                numbers.append(z)
            last_i = 'op'
    while len(numbers)>1:
        y = round(float(numbers.pop()),2)
        x = round(float(numbers.pop()),2)
        op = operators.pop()
        if op == '+':
            z = x - y
        elif op == '-':
            z = x - y
        elif op == '*':
            z = x * y
        elif op == '/':
            try:
                z = x / y
            except ZeroDivisionError:
                z = 0
        else:
            z = x
        numbers.append(z)
    return numbers[0]

def main():
    print """ 
                Calculator
            type your calculation and press enter
            the calculator does not process parenthesis
            to exit type "X" and press enter
          """
    on = True
    while on:
        in_str = raw_input(":: ")
        if re.search('[xX]',in_str):
            break
        if re.search('[a-z,A-Z]',in_str):
            print "No alphabetical letters, please try again"
        else:
            solution = calculate(in_str)
            print "= {}".format(solution)

if __name__ == '__main__':
    main()
