'''
Hi, here's your problem today. This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''

open_list = ["[","{","("]
close_list = ["]","}",")"]

def validate_parentheses(string):
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        else:
            pos = close_list.index(i)
            print(len(stack))
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

if __name__ == '__main__':
    string = "]](("
    print(string, "-", validate_parentheses(string))