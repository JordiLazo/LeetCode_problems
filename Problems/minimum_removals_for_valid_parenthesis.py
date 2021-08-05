'''
Hi, here's your problem today. This problem was recently asked by Uber:

You are given a string of parenthesis. Return the minimum number of parenthesis that would need
to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("

'''

def minRemoveToMakeValid(s):
    stack = []
    N = len(s)
    S = list(s)

    for i in range(N):
        if S[i] == "(":
            stack.append(i)
        elif S[i] == ")":
            if stack:
                stack.pop()
            else:
                S[i] = ""

    for j in stack:
        S[j] == ""

    return "".join(S)

if __name__ == '__main__':
    print(minRemoveToMakeValid("()())()"))
    print(minRemoveToMakeValid("a)b(c)d"))