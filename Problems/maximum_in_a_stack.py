'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max()
which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.
'''

class MaxStack:
  def __init__(self):
    self.mainStack = []
    self.cacheStack = []

  def push(self, val):
      self.mainStack.append(val)
      if (len(self.mainStack) == 1):
        self.cacheStack.append(val)
        return

      if(val > self.cacheStack[-1]):
        #Negative numbers mean that you count from the right instead of the left.
        # So, list[-1] refers to the last element, list[-2] is the second-last, and so on.
        self.cacheStack.append(val)

      else:
        self.cacheStack.append(self.cacheStack[-1])

  def pop(self):
    self.mainStack.pop()
    self.cacheStack.pop()


  def max(self):
    return self.cacheStack[-1]

if __name__ == '__main__':

  s = MaxStack()
  s.push(1)
  s.push(2)
  s.push(3)
  s.push(2)
  print(s.max())
  # 3
  s.pop()
  s.pop()
  print(s.max())
  # 2