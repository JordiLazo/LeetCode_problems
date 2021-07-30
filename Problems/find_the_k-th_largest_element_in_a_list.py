'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
'''

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == '__main__':

    print(findKthLargest([3, 5, 2, 4, 6, 8], 2))
    # 5
    print(findKthLargest([19, 12, 3, 5],1))
    #19

