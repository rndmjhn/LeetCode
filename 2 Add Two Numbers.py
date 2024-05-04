# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from multiprocessing.dummy import current_process


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        class Node:

            def __init__(self, data):
               self.data = data
               self.next = None

        class LinkedList:

            def __init__(self):
                self.head = None

            def reverse(self):
                prev = Nonecurrent = self.head
                while(current is not None):
                    next  = current.next
                    current.next = prev
                    prev = current
                    current = next
                self.head = prev

            def push(self, new_data):
                new_node = Node(new_data)
                new_node.next = self.head
                self.head = new_node


llist1 = LinkedList()
llist.push(2)
llist.push(4)
llist.push(3)

llist2 = LinkedList()
llist.push(5)
llist.push(6)
llist.push(4)

llist1.printList()



