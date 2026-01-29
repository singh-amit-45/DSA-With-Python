# Singly Linked List add node at the end and display the list

class node :
    def __init__(self, info, next = None) :
        self.info = info
        self.next = next
class singlyLinkdList :
    def __init__(self,head = None) :
        self.head = head

    def insertAtEnd(self, data) :
        temp = node(data)
        if (self.head != None) :
            t1 = self.head
            while (t1.next != None) :
                t1 = t1.next
            t1.next = temp
        else :
            self.head = temp
    def display(self) :
        t1 = self.head
        while (t1 != None) :
                print(t1.info)
                t1 = t1.next
obj = singlyLinkdList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.display()