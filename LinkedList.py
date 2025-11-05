from typing import Optional
class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional['Node'] = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        """
        Funtion finds middle node of linked list by using two pointer approach.
        One pointer moves slow and second pointer moves fast.
        When fast pointer reaches end of linked list our slow pointer is at middle.
        """
        temp = self.head
        forward =self.head
        if self.head is None:
            return False
        while forward is not None and forward.next is not None:
            temp = temp.next
            forward = forward.next.next
        return temp
    
def find_kth_from_end(ll, k):    
    """
    Function to find kth node from end of linked list.
    It uses two pointer approach also. We takes that 1 from end is same as last one.
    First we move fast pointer to k node. Then we move both slow pointer and fast pointer until end.
    When fast pointer reaches end our slow pointer is at kth node from end."""   
    slow = ll.head
    fast = ll.head
        
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
            
    return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

#print( my_linked_list.find_middle_node().value )

k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)





"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""