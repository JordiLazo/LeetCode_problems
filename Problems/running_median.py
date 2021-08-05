'''
Hi, here's your problem today. This problem was recently asked by Google:

You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
'''
from heapq import heappush, heappop

def runningMedian(a):
    minheap = []
    maxheap = []
    result = []
    def addnum(num,minheap,maxheap):
        if not maxheap or num < -maxheap[0]:
            heappush(maxheap, -num)
        else: heappush(minheap,num)

    def balance(minheap,maxheap):
        if len(minheap) - len(maxheap) >= 2:
            heappush(maxheap, -heappop(minheap))
        if len(maxheap) - len(minheap) >= 2:
            heappush(minheap, -heappop(maxheap))

    def getmedian(minheap,maxheap):
        if len(minheap) == len(maxheap):
            return (minheap[0] - maxheap[0]) / 2
        elif len(maxheap) > len(maxheap):
            return float(minheap[0])
        else: return float(-maxheap[0])
    for num in a:
        addnum(num,minheap,maxheap)
        balance(minheap,maxheap)
        result.append(getmedian(minheap,maxheap))

    return result


if __name__ == '__main__':
    print(runningMedian([2, 1, 4, 7, 2, 0, 5]))
    # 2 1.5 2 3.0 2 2.0 2
