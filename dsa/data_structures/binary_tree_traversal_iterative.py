from binary_tree import BinaryTree

class BinTree(BinaryTree):

    def pre_order_traversal(self):
        stack = []
        stack.insert(0, self)
        while len(stack) > 0:
            curr = stack[0]
            stack = stack[1:]                       # pop (root) from stack
            print(curr.get_val(), end = ' ')
            if curr.get_right() is not None:        # We stack right first then left
                stack.insert(0, curr.get_right())
            if curr.get_left() is not None:
                stack.insert(0, curr.get_left())
    
    
    def in_order_traversal(self):
        stack = []
        stack.insert(0, self)
        while len(stack) > 0:
            curr = stack[0]                        # top of stack
            if curr.get_left() is not None:
                stack.insert(0, curr.get_left())    # We stack only left
                curr = curr.get_left()
            else:
                print(curr.get_val(), end = ' ')
                stack = stack[1:]                   # pop left child from stack
                curr = stack[0]
                print(curr.get_val(), end = ' ')
                stack = stack[1:]                   # pop root from stack
                if curr.get_right() is not None:    # We stack right after printing root
                    stack.insert(0, curr.get_right())


    def level_order_traversal(self):
        queue = []
        queue.insert(0, self)
        while len(queue) > 0:
            curr = queue[0]                     # top of queue
            queue = queue[1:]                   # dequeue
            print(curr.get_val(), end = ' ')
            if curr.get_left() is not None:     # We queue right after printing root
                queue.append(curr.get_left())
            if curr.get_right() is not None:
                queue.append(curr.get_right())


    def post_order_traversal(self):
        # push root -> push right child -> push left child 
        # -> pop left child -> pop right child -> pop root    ## reverse order of insert/push

        stack = []
        queue = []
        stack.insert(0, self)

        while len(stack) > 0:
            curr = stack[0]                     # not pop yet

            # if curr.get_right() is not None or curr.get_left() is not None:
            if curr.get_right() is not None and curr.get_right().get_val() not in queue:
                stack.insert(0, curr.get_right())
            if curr.get_left() is not None and curr.get_left().get_val() not in queue:
                stack.insert(0, curr.get_left())
            
            # else:
            if (curr.get_right() is None or curr.get_right().get_val() in queue) \
                    and (curr.get_left() is None or curr.get_left().get_val() in queue):
                curr = stack[0]
                stack = stack[1:] # pop now that no children left to traverse
                queue.append(curr.get_val())

        while len(queue) > 0:
            print(queue.pop(0), end = ' ')



if __name__ == "__main__":
    
    root = BinTree(1)
    left_node1 = BinTree(2)
    right_node1 = BinTree(3)
    left_node2 = BinTree(4)
    right_node2 = BinTree(5)
    left_node3 = BinTree(6)
    
    root.set_left(left_node1)
    root.set_right(right_node1)    

    left_node1.set_left(left_node2)
    left_node1.set_right(right_node2)

    right_node1.set_left(left_node3)

    print("\nIterative Pre order traversal")
    print("\nPre order traversal")
    root.pre_order_traversal()
    print("\nIn order traversal")
    root.in_order_traversal()
    print("\nLevel order traversal")
    root.level_order_traversal()
    print("\nPost order traversal")
    root.post_order_traversal()