'''
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given an array of integers. Return the smallest positive integer that is not present in the array.
The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
'''

def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        correctPos = nums[i] -1
        while 1 <= nums[i] <= n and nums[i] != nums[correctPos]:
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i] - 1
    for i in range(n):
        if i +1 != nums[i]:
            return i +1
    return n +1
if __name__ == '__main__':
    print(first_missing_positive([3, 4, -1, 1]))
    # 2
