class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST():
    def __init__(self, root): # self는 instance를 나타내는 듯?
        self.root = root

    def search(self, value):
        node = self.root
        
        while node:
            temp = node
            if node.value == value:
                return node
            elif node.value > value:
                node = node.left
                node.parent = temp
            else:
                node = node.right
                node.parent = temp   

        return False

    def insert(self, value):
        node = self.root
        while True:
            if value < node.value:
                if node.left != None:
                    node = node.left
                else:
                    node.left = Node(value)
                    break
            else:
                if node.right != None:
                    node = node.right
                else:
                    node.right = Node(value)
                    break

    def delete(self, value):
        
        node = self.search(value)
        if node == False:
            return False
        parent = node.parent
        
        # non-chile
        if node.left == None and node.right == None:
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None
        
        # one left child
        if node.left != None and node.right == None:
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
        
        # one right child
        if node.left == None and node.right != None:
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right     

        # two child
        if node.left != None and node.right != None:
            new = node.right
            new_parent = node.right
            while new.left != None:
                new_parent = new
                new = new.left # find successor
                
            if new.right != None:
                new_parent.left = new.right
            else:
                new_parent.left = None
            
            if value < parent.value:
                parent.left = new # node delete and connect to new node
                new.left = node.left # copy left
                new.right = node.right # copy right
            else:
                parent.right = new
                new.left = node.left
                new.right = node.right

        return True

    def parent_value(self, value):
        temp = bst.search(value)
        if temp.parent != None: print(temp.parent.value)
        else: print(None)
        return

    def left_value(self, value):
        temp = bst.search(value)
        if temp.left != None: print(temp.left.value)
        else: print(None)
        return

    def right_value(self, value):
        temp = bst.search(value)
        if temp.right != None: print(temp.right.value)
        else: print(None)
        return
              
        
if __name__ == "__main__":

    root = Node(1) 
    bst = BST(root) # root를 node(1)로 선언
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.parent_value(3)
    bst.delete(4)
    bst.parent_value(3)
    bst.left_value(3)
    
    
