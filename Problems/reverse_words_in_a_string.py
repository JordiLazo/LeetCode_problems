'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
'''
def reverseWords(str):
    result, i,n = '',0,len(str)
    while i < n:
        while i < n and str[i] == ' ':
            i += 1
        if i >= n:
            break
        j = i +1
        while j < n and str[j] != ' ':
            j += 1
        sub = str[i:j]
        if len(result) == 0:
            result = sub
        else:
            result = sub + " " + result
        i = j+1
    return result



if __name__ == '__main__':
    print(reverseWords("The cat in the hat"))
    print(reverseWords("the sky is blue"))