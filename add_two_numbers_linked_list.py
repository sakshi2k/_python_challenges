# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        temp = head
        carry = 0
        
        while bool (l1 or l2 or carry):
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
                
            if l2:
                val += l2.val
                l2 = l2.next

            if carry != 0:
                val += carry
                carry = 0
            
            if(val >= 10):
                carry = 1
                val %= 10

            curr_node = ListNode(val)

            if head.next == None:       ## or temp.next 
                head.next = curr_node
                temp.next = curr_node

            temp.next = curr_node
            temp = temp.next

        return head.next


def insert_at_end(head, item):
    curr_node = ListNode(item)
    if head.next == None:
        head.next = curr_node
    else:
        prev_node = head.next
        head.next = curr_node
        curr_node.next = prev_node


def create_linked_list(arr: list) :
    head = ListNode()
    for item in arr:
        insert_at_end(head, item)

    return head


def print_list(idx, l_list_head) :
    l_list_head = l_list_head.next
    _str = ""
    while l_list_head != None:
        _str = _str + str(l_list_head.val) + " -> "
        l_list_head = l_list_head.next
    
    print(f"i = {i+1}  : f{_str}")
    return _str
 

if __name__ == "__main__":
    s = Solution()

    first_list_input = [
        create_linked_list([3, 4, 2]),
        create_linked_list([0]),
        create_linked_list([9, 9, 9, 9, 9, 9, 9]),
    ]

    second_list_input = [
        create_linked_list([4, 6, 5]),
        create_linked_list([0]),
        create_linked_list([9, 9, 9, 9]),
    ]

    output_list = [
        "7 -> 0 -> 8 -> " ,
        "0 -> ",
        "8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> ",
    ]

    for i in range(0, len(first_list_input)):
        head = s.addTwoNumbers(first_list_input[i], second_list_input[i])
        assert print_list(i, head) == output_list[i]
