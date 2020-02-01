class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value 

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node.left:
            print(node.value)
        if node.left and node.right:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)
        elif node.left:
            node.in_order_print(node.left)
            print(node.value)
        elif node.right:
            node.in_order_print(node.right)

        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            cur_node = q.dequeue()
            print(cur_node.value)
            if cur_node.left:
                q.enqueue(cur_node.left)
            if cur_node.right:
                q.enqueue(cur_node.right)
       

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.len() > 0:
            cur_node = s.pop()
            print(cur_node.value)
            if cur_node.left:
                s.push(cur_node.left)
            if cur_node.right:
                s.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# test = BinarySearchTree(5)

# test.insert(10)
# test.insert(3)
# test.insert(2)
# test.insert(4)
# test.insert(6)
# test.insert(7)

# def call_back(n):

#     print(n.value*2)

# test.for_each(call_back)

# call_back(test)

# test.bft_print(test)