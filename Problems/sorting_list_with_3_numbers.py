'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
'''

def sortNums(nums):
    num_one = 0
    num_two = 0
    num_three = 0

    for n in nums:
        if n == 1:
            num_one += 1
        elif n == 2:
            num_two += 1
        elif n == 3:
            num_three += 1

    return [1]*num_one + [2]*num_two + [3]*num_three

if __name__ == '__main__':

    print(sortNums([3,3,3,2,1,2,3,1]))
    # [1, 1, 2, 2, 3, 3, 3]