from abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    # Constructor
    def __init__(self, sourceCollection = None):
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        self.push(item)