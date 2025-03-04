from typing import Optional

class BinaryTree:
    def __init__(self, item = None) -> None:
        self.val :int = item
        self.__left : 'Optional[BinaryTree] | None' = None
        self.__right : 'Optional[BinaryTree] | None' = None
        self.__parent : 'Optional[BinaryTree] | None' = None

    def is_root(self) -> bool:
        return self.__parent is None

    def get_val(self) -> 'BinaryTree | None':
        return self.val

    def get_right(self) -> 'BinaryTree | None':
        return self.__right

    def get_left(self) -> 'BinaryTree | None':
        return self.__left

    def get_parent(self) -> 'BinaryTree | None':
        return self.__parent

    def get_root(self) -> 'BinaryTree | None':
        node = self
        while not node.is_root():
            node = node.get_parent()
        print(node.get_val())

    def set_right(self, node: 'Optional[BinaryTree] | None' ) -> 'BinaryTree | None':
        if(self.__right is None):
            self.__right = node
            node.__parent = self
        else:
            raise Exception('Right Node already exists')

    def set_left(self, node: 'Optional[BinaryTree] | None' ) -> 'BinaryTree | None':
        if(self.__left is None):
            self.__left = node
            node.__parent = self
        else:
            raise Exception('Left Node already exists')

    def set_root(self) -> 'BinaryTree | None':
        return self.root

        

if __name__ == "__main__":
    
    root = BinaryTree(1)
    left_node1 = BinaryTree(2)
    right_node1 = BinaryTree(3)
    left_node2 = BinaryTree(4)
    right_node2 = BinaryTree(5)
    left_node3 = BinaryTree(6)
    
    root.set_left(left_node1)
    root.set_right(right_node1)    

    left_node1.set_left(left_node2)
    left_node1.set_right(right_node2)

    right_node1.set_left(left_node3)

    print('\nRoot node from arbitrary node')
    right_node2.get_root()