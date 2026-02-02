#in singly linked list add nodein begin and display the list 

class node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class singlyLinkedList:
    def __init__(self, head=None):
        self.head = head

   
    def insertAtEnd(self, data):
        temp = node(data)

        if self.head is None:   
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp

    def insertAtbegin(self, data):
        temp = node(data)
        temp.next = self.head
        self.head = temp


    def display(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info, end=" -> ")
            t1 = t1.next
        print("None")


obj = singlyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtbegin(5)
obj.display()
