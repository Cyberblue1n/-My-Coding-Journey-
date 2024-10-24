class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def printlist(self):
        if self.head is None:
            print("List is empty")
            return 
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
if __name__ == "__main__":
    a = linked_list()
    a.insert_at_begin(10)
    a.insert_at_end(20)
    a.insert_at_end(30)
    a.insert_at_begin(1)
    a.printlist()

