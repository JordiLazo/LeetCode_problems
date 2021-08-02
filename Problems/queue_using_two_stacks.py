'''
Hi, here's your problem today. This problem was recently asked by Apple:

Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out).
Your class should support the enqueue and dequeue methods like a standard queue.
'''


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(val)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            print("Q is empty")
        x = self.s1[-1]
        self.s1.pop()
        return x


# Fill this in.
if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    # 1 2 3
