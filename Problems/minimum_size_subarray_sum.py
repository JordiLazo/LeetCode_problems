'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''
import sys


class Solution:
  def minSubArrayLen(self, s, nums):
      if s > sum(nums):
          return 0
      left = right = 0
      running_sum = 0
      result = sys.maxsize
      n = len(nums)

      while right < n:
          running_sum += nums[right]

          while running_sum >= s:
              result = min(result,right-left+1)
              running_sum -= nums[left]
              left += 1
          right += 1

      return result

if __name__ == '__main__':

    print(Solution().minSubArrayLen(12, [2, 3, 1, 2, 4, 3]))
    # 2

