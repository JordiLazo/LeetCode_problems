'''
Hi, here's your problem today. This problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False
def find(root,level,maxLevel,res):
    if(root != None):
        level += 1
        find(root.left, level, maxLevel, res)

        if(level > maxLevel[0]):
            res[0] = root.data
            maxLevel[0] = level
        find(root.right, level, maxLevel,res)

def deepestNode(root):
    res = [-1]
    maxLevel = [-1]
    find(root, 0, maxLevel,res)
    return res[0]

if __name__ == '__main__':


    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print(deepestNode(root))
    # (d, 3)