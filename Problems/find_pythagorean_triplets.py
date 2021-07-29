'''
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 52 + 122 = 132.
'''

def findPythagoreanTriplets(nums):
    j = 0

    for i in range(len(nums) - 2):
        for k in range(j+1, len(nums)):
            for j in range(i+1, len(nums) - 1):
                x = nums[i]*nums[i]
                y = nums[j]*nums[j]
                z = nums[k]*nums[k]
                if(x == y+z or y == x+z or z == x+y):
                    return True
    return False
  # Fill this in.

if __name__ == '__main__':
    print(findPythagoreanTriplets([3, 12, 5, 13]))
    # True

    print(findPythagoreanTriplets([10, 4, 6, 12, 5]))
    # False