from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        print("Value Inserted!!")

    def delBegin(self):
        if self.head is None:
            print("Empty List")
            return None
        else:
            temp = self.head
            value = self.head.data
            self.head = self.head.next
            del temp
            return value

    def delVal(self, value):
        if self.head is None:
            print("Empty List")
            return
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            del temp
            print('Value Deleted!!')
        else:
            current = self.head
            prev = None
            while current != None and current.data != value:
                prev = current
                current = current.next
            if current != None:
                prev.next = current.next
                del current
                print('Value:', value, 'Deleted!!')
            else:
                print('Value not Found!!')

    def __str__(self):
        current = self.head
        result = ''
        if current != None:
            while current.next != None:
                result += str(current.data) + '->'
                current = current.next
            result += str(current.data)
        else:
            result = 'Empty List'
        return result
