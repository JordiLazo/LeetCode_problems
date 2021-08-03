'''
Hi, here's your problem today. This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

def sortColors(nums):
    red = 0
    white = 0
    blue = len(nums) -1

    while white <= blue:
        curr = nums[white]
        if curr == 0:
            nums[white] = nums[red]
            nums[red] = 0
            red += 1
            white += 1
        elif curr == 1:
            white += 1
        else:
            nums[white] = nums[blue]
            nums[blue] = 2
            blue -= 1

if __name__ == '__main__':
    nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    print("Before Sort: ")
    print(nums)
    # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

    sortColors(nums)
    print("After Sort: ")
    print(nums)
    # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]