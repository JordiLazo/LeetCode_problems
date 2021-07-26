'''Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
'''

def longestPalindrome(s):
    def helper(l,r):
        while(l >= 0 and r<len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        test = helper(i,i)
        if len(test) > len(res):
            res = test
        test = helper(i, i+1)
        if len(test) > len(res):
            res = test
    return res

if __name__ == '__main__':
    string = "million"
    print(longestPalindrome(string))
    string = "banana"
    print(longestPalindrome(string))