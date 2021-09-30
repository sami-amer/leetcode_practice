class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):
    firstResult = l1.val + l2.val
    outInts= [l1.val + l2.val]
    return add(l1.next, l2.next, outInts)

def add(l1,l2,outInts):

    if l1.val == None and l2.val == None:
        return outInts    
    
    if l1.val == None:
        outInts.append(l2.val)
        return add(None, l2.next)
    
    if l2.val == None:
        outInts.append(l1.val)
        return add(l1.next, None)

    if l1.val + l2.val <10:
        outInts.append(l1.val+l2.val)
        return add(l1.next, l2.next)


if __name__ == '__main__':
    L1 = ListNode(2,ListNode(4,3))
    L2 = ListNode(5,ListNode(6,4))
    addTwoNumbers(L1,L2)   
    