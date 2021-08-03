'''
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root,
and all values in the right subtree are greater than or equal to the root.
'''

class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
def isValidBST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.key <= prev.key:
            return False
        prev = root
        root = root.right
    return True

if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(4)
    print(isValidBST(a))
    print(isValidBST(root))

    #    5
    #   / \
    #  3   7
    # / \ /
    # 1  4 6