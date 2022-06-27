class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVL():

    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0
        
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def search(self, key):
        target = self.node
        while target:
            temp = target
            if target.key == key:
                return target
            elif target.key > key:
                target = target.left.node
                target.parent = temp
            else:
                target = target.right.node
                target.parent = temp   

        return False
    
    def insert(self, key):
        tree = self.node
        new = Node(key)

        if tree == None:
            self.node = new
            self.node.left = AVL()
            self.node.right = AVL()
        elif key < tree.key: # left child
            self.node.left.insert(key) # recursive
        elif key > tree.key: # right child
            self.node.right.insert(key)
        else:
            print("this key is already exist in tree")
            return None

        self.balancing()

    def delete(self, key):   
        
        if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # no child
                elif self.node.left.node == None:
                    self.node = self.node.right.node # parent to right child
                elif self.node.right.node == None:
                    self.node = self.node.left.node # parent to left child
                else: # two child
                    successor = self.find_successor(self.node)
                    if successor != None:
                        self.node.key = successor.key
                        self.node.right.delete_node(successor.key) # origin successor delete
                
                self.balancing()
                return

            elif key < self.node.key:
                self.node.left.delete_node(key) # recursive
            elif key > self.node.key:
                self.node.right.delete_node(key)

            self.balancing()
        else:
            return None

    def find_successor(self, node):
        node = node.right.node
        if node != None:
            while node.left != None:
                if node.left.node != None:
                    node = node.left.node
                else:
                    return node
        return node

    def get_height(self):
        if self.node:
            return self.height
        else: 
            return 0

    def balancing(self):

        self.update_h(False)
        self.update_b(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_h()
                    self.update_b()
                self.rotate_right()
                self.update_h()
                self.update_b()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_h()
                    self.update_b()
                self.rotate_left()
                self.update_h()
                self.update_b()

    def update_h(self, recurs=True): # default bool = True 
        if self.node != None:
            if recurs:
                if self.node.left != None:
                    self.node.left.update_h()
                if self.node.right != None:
                    self.node.right.update_h()
            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_b(self, recurs=True):
        if not self.node == None:
            if recurs:
                if self.node.left != None:
                    self.node.left.update_b()
                if self.node.right != None:
                    self.node.right.update_b()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_left(self):
        a = self.node
        b = self.node.right.node
        t = b.left.node

        self.node = b
        b.left.node = a
        a.right.node = t
    
    def rotate_right(self):
        a = self.node
        b = self.node.left.node
        t = b.right.node

        self.node = b
        b.right.node = a
        a.left.node = t

if __name__ == "__main__":


    arr = [1, 2, 4, 6]

    avl = AVL(arr)
    avl.insert(5)
    print(avl.search(2).left.node.key)
    
    
