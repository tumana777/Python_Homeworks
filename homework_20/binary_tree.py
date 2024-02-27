# Create Node Class
class TreeNode:
    # Initialize parameters
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
# Create BinaryTree Class
class BinaryTree:
    # Initialize parameters
    def __init__(self):
        self.root = None
        
    # Define insert method for calling outside this class
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    # Define protected insert method to call inside this class
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            
        return node
    
    # Define method to print parents calling outside this class
    def printParents(self):
        print("The Parents Are: ")
        self._printParents(self.root, None)
    
    # Define protected parent print method to call inside this class
    def _printParents(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)
                
            self._printParents(node.left, node)
            self._printParents(node.right, node)
            
    # Define method to print children to call outside this class
    def printChildren(self):
        print("Printing Children Nodes: ")
        self._printChildren(self.root)
        
    # Define protected children print method to call inside this class
    def _printChildren(self, node):
        if node:
            print(node.key, "-> ", end="")
            if node.left is not None:
                print(node.left.key, "-> ", end="")
            if node.right is not None:
                print(node.right.key, "-> ", end="")
            print()
                
            self._printChildren(node.left)
            self._printChildren(node.right)
    
    # This method prints leaves, calling outside this class
    def print_leaves(self):
        if self.root:
            print("Printing Leaf Nodes: ")
            self._print_leaves(self.root)
            print()
    
    # This protected method prints leaves, calling inside this class
    def _print_leaves(self, node):
        if node:
            if not node.left and not node.right:
                print(node.key, end=" ") 
            self._print_leaves(node.left)
            self._print_leaves(node.right)
    
    # This method calls protexted _count_edges method and returns number of edges
    def count_edges(self):
        if self.root:
            return self._count_edges(self.root) - 1
        else:
            return 0
    
    # Define protected method to count edges of nodes
    def _count_edges(self, node):
        if node is None:
            return 0
        return 1 + self._count_edges(node.left) + self._count_edges(node.right)
    
    # This method prints number of edges of nodes
    def print_edges(self):
        if self.root:
            print("Number of edges in the tree:", self.count_edges())

            
# Create BinaryTree object
binary = BinaryTree()

# Insert nodes in binary tree
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
binary.insert(1)

# Printing parents, children, leaves and edges
binary.printParents()
binary.printChildren()
binary.print_leaves()
binary.print_edges()
