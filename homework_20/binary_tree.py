class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            
        return node
    
    def printParents(self):
        print("The Parents Are: ")
        self._printParents(self.root, None)
        
    def _printParents(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)
                
            self._printParents(node.left, node)
            self._printParents(node.right, node)
            
    def printChildren(self):
        print("Printing Children Nodes: ")
        self._printChildren(self.root)
        
    def _printChildren(self, node):
        if node is not None:
            print(node.key, "-> ", end="")
            if node.left is not None:
                print(node.left.key, "-> ", end="")
            if node.right is not None:
                print(node.right.key, "-> ", end="")
            print()
                
            self._printChildren(node.left)
            self._printChildren(node.right)
            
binary = BinaryTree()
binary.insert(5)
binary.insert(3)
binary.insert(9)
binary.insert(2)
binary.insert(10)
binary.insert(6)
binary.insert(4)
binary.insert(7)
binary.insert(12)
binary.insert(18)
binary.insert(11)

'''
                   5
            3            9
        2     4   |6           10
                        7|11         12
                                        18

'''

binary.printParents()
binary.printChildren()