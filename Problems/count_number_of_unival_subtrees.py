'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)
'''


class Node:
    # Utility function to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# This function increments count by number of single
# valued subtrees under root. It returns true if subtree
# under root is Singly, else false.
def countSingleRec(root, count):
    # Return False to indicate None
    if root is None:
        return True

    # Recursively count in left and right subtress also
    left = countSingleRec(root.left, count)
    right = countSingleRec(root.right, count)

    # If any of the subtress is not singly, then this
    # cannot be singly
    if left == False or right == False:
        return False

    # If left subtree is singly and non-empty , but data
    # doesn't match
    if root.left and root.data != root.left.data:
        return False

    # same for right subtree
    if root.right and root.data != root.right.data:
        return False

    # If none of the above conditions is True, then
    # tree rooted under root is single valued,increment
    # count and return true
    count[0] += 1
    return True


# This function mainly calss countSingleRec()
# after initializing count as 0
def countSingle(root):
    # initialize result
    count = [0]

    # Recursive function to count
    countSingleRec(root, count)

    return count[0]


if __name__ == '__main__':
    """Let us construct the below tree
                5
              /   \
            4       5
           /  \      \
          4    4      5
    """
    root = Node(5)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(4)
    root.right.right = Node(5)
    countSingle(root)
    print("Count of Single Valued Subtress is", countSingle(root))

    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)
    a.right.left = Node(1)
    a.right.right = Node(0)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)

    print(countSingle(a))
    # 5