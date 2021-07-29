'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''

def searchRange(array, target):
    if not array:
        return [-1,-1]
    N = len(array)
    st, end = -1, -1
    l,r = 0, N

    #binary search left
    while l < r:
        mid = (l+r)//2
        if array[mid] >= target:
            r = mid
        else:
            l = mid+1
    if l < N and array[l] == target:
        st = l
    #binary search right
    l, r = 0, N
    while l < r:
        mid = (l+r)//2
        if array[mid] <= target:
            l = mid+1
        else:
            r = mid
    if array[r-1] == target:
            end = r-1
    return [st,end]

if __name__ == '__main__':
    a = [100, 150, 150, 153]
    b = 150

    print("Output:",searchRange(a,b))