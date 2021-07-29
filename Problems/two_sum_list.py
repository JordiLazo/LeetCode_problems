'''
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
'''
class Solution:
    def bruteForceTwoSum(array,target):
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                sum = array[i] + array[j]
                if sum == target:
                    return True
                else:
                    return False

    def two_sum(array, target):
        values = dict()

        for i, elem in enumerate(array):
            comp = target - elem

            if comp in values:
                return [values[comp], i]

            values[elem] = i
        return []

    # Fill this in.

if __name__ == '__main__':
    array = [4,7,1,-3,2]
    target = 11
    print (Solution.bruteForceTwoSum(array,target))
    print(Solution.two_sum(array, target))
    # True

