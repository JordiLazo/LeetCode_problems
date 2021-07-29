'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
'''

def singleNumber(array):
    result = array[0]
    for i in range(1,len(array)):
        result ^= array[i]
    return result

if __name__ == '__main__':
    array = [2,2,1,0,1,3,3,7,8,8,9,9,7,6,6]
    print(singleNumber(array))