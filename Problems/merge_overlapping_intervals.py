'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).
'''


def merge(intervals):
    if intervals == []:
        return []
    result = []
    intervals.sort()
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

if __name__ == '__main__':
    print(merge([[1, 3], [5, 8], [4, 10], [20, 25]]))
    # [(1, 3), (4, 10), (20, 25)]
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    # [[1,6],[8,10],[15,18]]

