from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length is 0:
            # Appending first value when
            # DLL is empty
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length < self.capacity:
            # When capacity of buffer HAS NOT been reached
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.current is self.storage.tail:
            # When capacity of buffer HAS been reached
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            # Add
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            # Removes unneeded next property 
            self.storage.delete(self.current.next)
            

    def get(self): #O(n)
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        curr = self.storage.head

        while curr is not None:
            list_buffer_contents.append(curr.value)
            curr = curr.next

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
