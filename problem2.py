class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next         

def addTwoNumbers(l1,l2):
    result = ListNode(0) # initialize the LinkedList
    result_tail = result
    carry = 0

    while l1 or l2 or carry: # *NOTE: instead of recursing, keep going until everything is NONE
        val1 = (l1.val if l1 else 0) # *NOTE: Use comprehension instead of if else statements for a cleaner line
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1 + val2 +carry, 10) #! NEW BUILT-IN: divmod returns quotient and remainder

        result_tail.next = ListNode(out) # We add the result to the initialized linked list
        result_tail = result_tail.next # We move our working list to the end of our linked list
        l1 = (l1.next if l1 else None) # Again, checking for None with comprehension
        l2 = (l2.next if l2 else None)
    
    return result.next # skips the first 0
        


if __name__ == '__main__':
    L1 = ListNode(2,ListNode(4,3))
    L2 = ListNode(5,ListNode(6,4))
    print(addTwoNumbers(L1,L2))
    