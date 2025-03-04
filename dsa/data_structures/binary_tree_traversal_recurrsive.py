from binary_tree import BinaryTree

class BinTree(BinaryTree):

    def get_val(self) -> 'BinaryTree | None':
        return self.val

    def get_right(self) -> 'BinaryTree | None':
        return self._BinaryTree__right

    def get_left(self) -> 'BinaryTree | None':
        return self._BinaryTree__left

    def get_pre_order_traversal(self):
        if self.val is not None:
            print(self.val, end=' ')
            if self.get_left() is not None:
                self.get_left().get_pre_order_traversal()
            if self.get_right() is not None:
                self.get_right().get_pre_order_traversal()
            
    def get_post_order_traversal(self):
        if self.val is not None:
            if self.get_left() is not None:
                self.get_left().get_post_order_traversal()
            if self.get_right() is not None:
                self.get_right().get_post_order_traversal()
            print(self.val, end = " ")
        

    def get_in_order_traversal(self):
        if self.val is not None:
            if self.get_left() is not None:
                self.get_left().get_post_order_traversal()
            print(self.val, end = " ")
            if self.get_right() is not None:
                self.get_right().get_post_order_traversal()
        
    def get_level_order_traversal(self):
        if self.val is not None:
            q = []
            q.append(self)
            while len(q):
                node: BinaryTree = q[0]
                q = q[1:]
                print(node.get_val(), end = ' ')
                if(node.get_left() is not None):
                    q.append(node.get_left())
                if(node.get_right() is not None):
                    q.append(node.get_right())



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

    print("\nRecursive tree traversal")

    print("\nPre order traversal")
    root.get_pre_order_traversal()
    print("\nPost order traversal")
    root.get_post_order_traversal()
    print("\nIn order traversal")
    root.get_in_order_traversal()

    print("\nLevel order traversal")
    root.get_level_order_traversal()