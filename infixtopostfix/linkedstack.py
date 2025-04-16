from abstractstack import AbstractStack
from node import Node

class LinkedStack(AbstractStack):
    def __init__(self,sourceCollection=None):
        self._items=None
        AbstractStack.__init__(self,sourceCollection)

    def push(self,item):
        self._items=Node(item,self._items)
        self._size+=1
        
    def pop(self):
        if self.isEmpty():
            raise KeyError("stack is empty")
        data=self._items.data
        self._items=self._items.next
        self._size-=1
        return data

    def __iter__(self):
        probe=self._items
        temp=[]
        while probe is not None:
            temp.append(probe.data)
            probe=probe.next
        return iter(reversed(temp))
    
    def peek(self):
        if self.isEmpty():
            raise KeyError("stack is empty")
        return self._items.data
    
    def clear(self):
        self._items=None
        self._size=0