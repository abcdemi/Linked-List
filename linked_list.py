# -*- coding: utf-8 -*-
"""
Linked list is a dynamic data structure. Easily updated, good for impementing
stacks, queues, lists. But they require extra memory, the access to the 
element is hard
"""

class Node:
    def __init__(self, value):
        self.item = value
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.start_node = None
        
    def traverse_linked_list(self):
        if self.start_node is None:
            return "The list has no elements"
        else:
            nodes = ""
            node = self.start_node
            while node is not None:
                nodes += str(node.item) + "\n"
                node = node.ref
            return nodes[0:-1]
        
    def insert_node_to_start(self, value):
        new_node = Node(value)
        new_node.ref = self.start_node
        self.start_node = new_node
        
    def insert_item_to_end(self, value):
        new_node = Node(value)
        if self.start_node is None:
            self.start_node = new_node
            return
        
        node = self.start_node
        while node.ref is not None:
            node = node.ref
        node.ref = new_node
        
    def insert_in_the_middle_after(self, previous_value, value):
        node = self.start_node
        while node is not None:
            if node.item == previous_value:
                break
            node = node.ref
        
        if node is None:
            print("The item is not in the list")
        else:
            new_node = Node(value)
            new_node.ref = node.ref
            node.ref = new_node
            
    def insert_in_the_middle_before(self, next_value, value):
        if self.start_node is None:
            print("The list is empty")
            return
        
        if next_value == self.start_node.item:
            new_node = Node(value)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        
        node = self.start_node
        while node.ref is not None:
            if node.ref.item == next_value:
                break
            node = node.ref
            
        if node.ref is None:
            print("The item not in the list")
        else:
            new_node = Node(value)
            new_node.ref = node.ref
            node.ref = new_node
            
    def insert_by_index(self, index, value):
        if index == 1:
            new_node = Node(value)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        
        i = 1
        node = self.start_node
        while i < index - 1 and node is not None:
            node = node.ref
            i = i + 1
        
        if node is None:
            print("The index out of range")
        else:
            new_node = Node(value)
            new_node.ref = node.ref
            node.ref = new_node
            
    def get_length(self):
        if self.start_node is None:
            return 0
        
        node = self.start_node
        count = 0
        while node is not None:
            count += 1
            node = node.ref
        
        return count
    
    def search_item(self, value):
        if self.start_node is None:
            print("The list has no elements")
            return
        
        node = self.start_node
        while node is not None:
            if node.item == value:
                print("The item is found")
                return True
            node = node.ref
        print("The item is not found")
        return False

    def make_a_new_linked_list(self):
        nums = int(input("Type in the number of nodes:"))
        if nums == 0:
            return
        else:
            for i in range(nums):
                value = int(input("Enter the value for the node:"))
                self.insert_item_to_end(value)

    def delete_at_start(self):
        if self.start_node is None:
            print("This list has no elements to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no elements to delete")
            return
        
        node = self.start_node
        while node.ref.ref is not None:
            node = node.ref
        node.ref = None

    def delete_element_by_value(self, value):
        if self.start_node is None:
            print("The list has no item to delete")
            return

        if self.start_node.item == value:
            self.start_node = self.start_node.ref
            return
        
        node = self.start_node
        while node.ref is not None:
            if node.ref.item == value:
                break
            node = node.ref
        
        if node.ref is None:
            print("Item is not on the list")
        else:
            node.ref = node.ref.ref

    def reverse_linked_list(self):
        prev_node = None
        current_node = self.start_node
        while current_node is not None:
            next_node = current_node.ref
            current_node.ref = prev_node
            prev_node = current_node
            current_node = next_node
        self.start_node = prev_node

        
if __name__ == '__main__':
    new_linked_list = LinkedList()
    new_linked_list.insert_item_to_end(5)
    new_linked_list.insert_node_to_start(10)
    new_linked_list.insert_by_index(1, 3)
    new_linked_list.insert_in_the_middle_after(3, 1)
    new_linked_list.insert_in_the_middle_before(1, 2)
    
    print(new_linked_list.traverse_linked_list())
    
    print(new_linked_list.search_item(5))
    
    new_linked_list.delete_element_by_value(2)
    print("====================")
    print(new_linked_list.traverse_linked_list())
    print("====================")
    
    new_linked_list.reverse_linked_list()
    print(new_linked_list.traverse_linked_list())
    print("length =", new_linked_list.get_length())
    print("====================")


    another_linked_list = LinkedList()
    another_linked_list.make_a_new_linked_list()
    print(another_linked_list.traverse_linked_list())
    print("++++++++++++++++++++")