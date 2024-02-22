
# Create node class
class Node:
    
    # Initialize parameters
    def __init__(self, data):
        self.data = data
        self.next = None

# Create LinkedList Class
class LinkedList:
    
    # Initialize head
    def __init__(self):
        self.head = None

    # This method adds new node object at the end of linked list
    def append(self, data):
        
        # Create new node object
        new_node = Node(data)

        # Validate if list is empty or not
        if self.head is None:
            self.head = new_node
            return

        # Imagine last node is always head
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    # This method adds new node object at given index
    def insert(self, data, index):
        
        # Create new node object
        new_node = Node(data)

        # Validate if given index is 0, insert new node at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0

        # Loop over the list to find given index 
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        # Insert new node
        new_node.next = current_node.next
        current_node.next = new_node


    # This method deletes node by given index
    def remove(self, index):
        
        # If given index is 0, first node will be removed 
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_index = 0

        # Loop over linked list to find index of node
        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next

        # If curren node is not last, link previous and next nodes
        if current_node.next:
            current_node.next = current_node.next.next
            
            
    # This method deletes node by given value
    def delete(self, value):
        
        # Untill loop, if given value equals first node data, removes it
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current_node = self.head 

        # Loop over the list
        while current_node.next:
            
            # If given value equals current node's data, breaks loop to store current node
            if current_node.data == value:
                break
            prev = current_node
            current_node = current_node.next
        
        # Validate if given value is in the linked list, remove current node, otherwise, do nothing
        if current_node.data == value:
            # Link current node's previous and next nodes
            prev.next = current_node.next

    # This method prints nodes 
    def display_info(self):
        
        current_node = self.head

        # Print nodes by while loop
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()
        
# Create LinkedList object
linked_list = LinkedList()

linked_list.append(5)
linked_list.append(10)
linked_list.append(2)

linked_list.display_info()

linked_list.insert(11, 1)
linked_list.insert(15, 2)
linked_list.display_info()

linked_list.remove(2)
linked_list.delete(11)
linked_list.delete(19)
linked_list.display_info()