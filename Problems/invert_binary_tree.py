'''
This problem was recently asked by Twitter:

You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.

Example:

    a
   / \
  b   c
 / \  /
d   e f

The inverted version of this tree is as follows:

  a
 / \
 c  b
 \  / \
  f e  d
'''


# A class to store a binary tree node
class Node:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right


# Function to perform preorder traversal on a given binary tree
def preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


# Utility function to swap left subtree with right subtree
def swap(root):
    if root is None:
        return

    temp = root.left
    root.left = root.right
    root.right = temp


# Function to invert a given binary tree using preorder traversal
def invertBinaryTree(root):
    # base case: if the tree is empty
    if root is None:
        return

    # swap left subtree with right subtree
    swap(root)

    # invert left subtree
    invertBinaryTree(root.left)

    # invert right subtree
    invertBinaryTree(root.right)


if __name__ == '__main__':
    ''' Construct the following tree
              a
            /   \
          b       c
         / \     / 
        d   e   f   
    '''

    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')

    preorder(root)
    print("\n")
    invertBinaryTree(root)
    preorder(root)

