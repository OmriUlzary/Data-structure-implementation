from stack import Stack
import json
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def __str__(self):
        temp = self.head
        linked_list_str = ''
        while temp is not None:
            linked_list_str = linked_list_str + str(temp.data) + ", "
            temp = temp.next
        return linked_list_str[:-2]

    def add_new_head(self, value):
        new_node = Node(value) # Create Node object with given value (6)
        new_node.next = self.head # Define next to new head
        self.head = new_node # init list head
        self.counter += 1

    def add_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        self.counter += 1

    def count(self):
        return self.counter

    def get_sub_item(self, item):
        new_linked_list = LinkedList()
        temp = self.head
        stack = Stack()
        count = 0
        if item < 1 or item > self.counter:
            return None
        else:
            while temp is not None:
                if count < (self.counter - item):
                    temp = temp.next
                    count += 1
                else:
                    stack.push(temp.data)
                    temp = temp.next
            while stack.size() != 0:
                new_linked_list.add_new_head(stack.pop())
            return new_linked_list


    def search_value(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def is_even(self):
         return self.counter % 2 == 0

    def split_linked_list(self, index):
        first_linked_list = LinkedList()
        second_linked_list = LinkedList()
        temp = self.head
        stack = Stack()
        if index <= 0 or index > self.counter:
            return None
        else:
            while temp is not None:
                stack.push(temp.data)
                temp = temp.next
            while stack.size() != 0:
                if index > stack.size():
                    first_linked_list.add_new_head(stack.pop())
                else:
                    second_linked_list.add_new_head(stack.pop())
            return "The first linked list is:" + " " + str(first_linked_list) + " " + "," + "The second linked list is:" + " " + str(second_linked_list)

    def serialize(self):
        # gets self return dict
        serialized_linked_list = {}
        temp = self.head
        while temp.next is not None:
            serialized_linked_list[temp.data] = temp.next.data
            temp = temp.next
        return serialized_linked_list

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.serialize(), file)


