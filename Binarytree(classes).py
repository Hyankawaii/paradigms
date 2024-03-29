class node:
    def __init__(self, item):
        self.left_pointer = None
        self.right_pointer = None
        self.item = item
    def insert(self, item):
        if self.item != None:
            if item < self.item:
                if self.left_pointer == None:
                    self.left_pointer = node(item)
                else:
                    self.left_pointer.insert(item)
            else:
                if self.right_pointer == None:
                    self.right_pointer = node(item)
                else:
                    self.right_pointer.insert(item)
        else:
            self.item = item
    def search(self, value):
        if value == self.item:
            print("value found in the tree")
        elif value > self.item and self.right_pointer != None:
            self.right_pointer.search(value)
        elif value < self.item and self.right_pointer != None:
            self.right_pointer.search(value)
        else:
            print("value not found")
        
        

tree = node(50)
print(tree.item)
tree.insert(5)
tree.insert(4)
tree.insert(70)
print(tree.right_pointer.item)
print(tree.left_pointer.left_pointer.item)
tree.search(7)