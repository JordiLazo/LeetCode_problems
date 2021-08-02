'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
'''
from collections import Counter


def buddyStrings(A, B):
    c1,c2 = Counter(A), Counter(B)
    if c1 != c2:
        return False
    diff = sum([1 for i in range(len(A)) if A[i] != B[i]])
    if diff == 2:
        return True
    elif diff == 0:
        any([cnt > 1 for char,cnt in c1.items()])
    else:
        return False


if __name__ == '__main__':
    print(buddyStrings('aaaaaaabc', 'aaaaaaacb'))
    # True
    print(buddyStrings('aaaaaabbc', 'aaaaaaacb'))
    # False