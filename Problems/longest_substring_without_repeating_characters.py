'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview,
though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
'''

class Solution:
  def lengthOfLongestSubstring(self, string):
      seen = {}
      maximum_lenght = 0
      start = 0

      for end in range(len(string)):
          if string[end] in seen:
              start = max(start,seen[string[end]] +1 )
          seen[string[end]] = end
          maximum_lenght = max(maximum_lenght, end-start +1)

      return maximum_lenght


if __name__ == '__main__':
    string = "jordilazo"
    print("The input string is", string)
    lenght = Solution().lengthOfLongestSubstring(string)
    print("The length of the longest non-repeating character" +" substring is ", lenght)