import json
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def __str__(self):
        temp = self.head
        doubly_linked_list_str = ''
        while temp is not None:
            doubly_linked_list_str = doubly_linked_list_str + str(temp.data) + ", "
            temp = temp.next
        return doubly_linked_list_str[:-2]

    def add_new_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.counter += 1

    def add_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.counter += 1


    def count(self):
        return self.counter

    def get_sub_item(self, items):
        new_linked_list = DoublyLinkedList()
        temp = self.tail
        index = 0
        if items < 1 or items > self.counter:
            return None
        else:
            while temp is not None and index < items:
                new_linked_list.add_new_head(temp.data)
                temp = temp.prev
                index += 1
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
        first_linked_list = DoublyLinkedList()
        second_linked_list = DoublyLinkedList()
        temp = self.tail
        start_index = self.counter - index
        count = 0
        if index < 1 or index - 1 > self.counter:
            return None
        else:
            while temp is not None:
                if count <= start_index:
                    second_linked_list.add_new_head(temp.data)
                    count += 1
                else:
                    first_linked_list.add_new_head(temp.data)
                temp = temp.prev
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



