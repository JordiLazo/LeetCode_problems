'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
'''

def maximum_product_of_three(nums):
  res = max(nums)
  curMin, curMax = 1,1

  for i in nums:
      if i == 0:
          curMin, curMax = 1,1
          continue
      tmp = curMax * i
      curMax = max(i*curMax, i* curMin,i)
      curMin = min(tmp, i* curMin, i)
      res = max(res,curMax)

  return res

if __name__ == '__main__':

    print(maximum_product_of_three([1, 3, 2, 8]))
    # 128

