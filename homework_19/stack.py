# Create node class
class Node:    
    # Initialize parameters
    def __init__(self, data):        
        self.data = data        
        self.next = None

# Create stack class
class Stack:    
    # Initialize parameters
    def __init__(self):        
        self.top_node = None        
        self.length = 0    
    
    # This method checks if stack is empty or not
    def empty(self):        
        return self.length == 0    
    
    # This method returns stack length
    def size(self):        
        return self.length    
    
    # This method returns last element  in stack
    def top(self):
        
        # Check stack is empty or not
        if not self.empty():            
            return self.top_node.data        
        else:            
            # If stack is empty, raise indexerror
            raise IndexError("Stack Is Empty")    
    
    # This method adds new node object at the top in stack
    def push(self, data):        
        
        # Create new node object and add at the top
        new_node = Node(data)        
        new_node.next = self.top_node        
        self.top_node = new_node        
        
        # Increse stack length
        self.length += 1    
    
    # This method removes node object from top and returns it
    def pop(self):        
        
        # Check if stack is empty or not
        if not self.empty():            
            popped_item = self.top_node.data            
            self.top_node = self.top_node.next            
            # Decrease stack length
            self.length -= 1            
            # Return removed node data
            return popped_item        
        else:            
            # If empty, raises indexerror
            raise IndexError("Stack Is Empty")
            
# Create stack object
stack = Stack()
print(stack.size())
stack.push(1)
stack.push(5)
stack.push(10)
print(stack.size())