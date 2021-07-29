'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

You are given a singly linked list and an integer k. Return the linked list, removing the k-th last element from the list.

Try to do it in a single pass and using constant space.

Examples:

Input: 2 -> 3 -> 1 -> 7 -> NULL, N = 1
Output:
The created linked list is:
2 3 1 7
The linked list after deletion is:
2 3 1

Input: 1 -> 2 -> 3 -> 4 -> NULL, N = 4
Output:
The created linked list is:
1 2 3 4
The linked list after deletion is:
2 3 4
'''

class Node:
  def __init__(self,new_data):
    self.data = new_data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,n):
        first = self.head
        second = self.head
        for i in range(n):
            if(second.next == None):
                if(i == n-1):
                    self.head = self.head.next
                return self.head
            second = second.next

        while(second.next != None):
            second = second.next
            first = first.next

        first.next = first.next.next

    def printList(self):
        tmp_head =self.head
        while(tmp_head != None):
            print(tmp_head.data, end = ' ')
            tmp_head = tmp_head.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print("Created Linked list is:")
    llist.printList()
    llist.deleteNode(1)
    print("\nLinked List after Deletion is:")
    llist.printList()