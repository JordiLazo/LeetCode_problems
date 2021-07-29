'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase.
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
'''


def staircase(n):
    if n <= 1:
        return n
    return staircase(n-1) + staircase(n-2)

def countWays(n):
    return staircase(n+1)

if __name__ == '__main__':

    print(countWays(4))
    # 5
    print(countWays(5))
    # 8