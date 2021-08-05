'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0.
Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
'''
def threeSum(nums):
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l,r = i+1 , len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res


if __name__ == '__main__':
    # Test Program
    nums = [1, -2, 1, 0, 5]
    nums2 = [0, -1, 2, -3, 1]
    print(threeSum(nums))
    # [[-2, 1, 1]]
    print(threeSum(nums2))
    # [0, -1, 1], [2, -3, 1]