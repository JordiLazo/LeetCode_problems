'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
  def moveZeros(self, nums):
      zero_count = nums.count(0)
      next_non_zero = 0

      for i in nums:
          if i != 0:
              nums[next_non_zero] = i
              next_non_zero += 1

      for zero in range(1, zero_count + 1):
          nums[-zero] = 0

if __name__ == '__main__':

    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().moveZeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]