from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    DEFAULT_CAPACITY=10
    def __init__(self,sourceCollection=None):
        self._items=Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self,sourceCollection)
    
    def __iter__(self):
        items=[]
        for i in range(self._size-1,-1,-1):
            items.append(self._items[i])
        return iter(items)
    
    def peek(self):
        if self.isEmpty():
            raise KeyError("stack is empty")
        
        return self._items[len(self)-1]
    
    def clear(self):
        self._size=0
        self._items=Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self,item):
        if self._size>=len(self._items):
            newSize= 2 * len(self._items)
            newItems = Array(newSize)
            for i in range(self._size):
                 newItems[i] = self._items[i]
            self._items = newItems  

        self._items[len(self)]=item
        self._size+=1

    def pop(self):
        if self.isEmpty():
            raise KeyError("stack is empty")
        
        removeItem=self._items[len(self)-1]
        self._items[self._size-1]=None
        self._size-=1

        return removeItem