class Node:

     def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
         self.head = None

    def reverse(self):
         prev = None
         current = self.head
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

    def printList(self):
        temp = self.head
        returner = ""
        while(temp):
            returner = str(returner) + str(temp.data)
            temp = temp.next
        return returner

    def returnanswer(self, answer):
        llanswer = LinkedList()
        for each in str(answer):
            llanswer.push(each)
        return llanswer
    

llist1 = LinkedList()
llist1.push(2)
llist1.push(4)
llist1.push(3)

llist2 = LinkedList()
llist2.push(5)
llist2.push(6)
llist2.push(4)

result = int(llist1.printList()) + int(llist2.printList())

output = LinkedList()
output.returnanswer(result)




