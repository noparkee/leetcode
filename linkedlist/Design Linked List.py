class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < len(self.a):
            return self.a[index]
        else:
            return -1
        
        

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.a.insert(0, val)
        

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.a.append(val)
        

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= len(self.a):
            self.a.insert(index, val)
        

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < len(self.a):
            self.a.pop(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)