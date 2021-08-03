'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a binary tree, return all values given a certain height h.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def valueAtHeight(root,height):
    level = []
    counter = 1
    level.append(root)
    while height != counter:
        n = len(level)
        for item in level:
            if item.left != None:
                level.append(item.left)
            if item.right != None:
                level.append(item.right)
        counter += 1
        level = level[n::]
    result = []
    for item in level:
        result.append(item.value)
    return result


if __name__ == '__main__':
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    print(valueAtHeight(a,3))
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   7

