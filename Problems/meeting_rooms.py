'''
Hi, here's your problem today. This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals for lectures.
The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
'''
def canAttendMeetings(intervals):
    intervals.sort()
    last_end = -1
    for start,end in intervals:
        if last_end <= start:
            last_end = end
        else:
            return False
    return True

if __name__ == '__main__':
    print(canAttendMeetings([(30, 75), (0, 50), (60, 150)]))


