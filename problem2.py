class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listify(L):
    output = []
    hold = []
    for elem in L:
        if hold:
            num = elem + hold[0]
            hold = []
        else:
            num = elem
        if num <10:
            output.append(num)
            continue
        elif num >= 10:
            output.append(0)
            hold.append(num - 9)
            continue
    return output
            
def addTwoNumbers(l1,l2):
    firstResult = l1.val + l2.val
    outInts= [l1.val + l2.val]
    return listify(add(l1.next, l2.next, outInts))

def add(l1,l2,outInts):
    try:
        outInts.append(l1.val + l2.val)
    except AttributeError:
        mod = []
        first = False
        second = False
        if type(l1) == int:
            mod.append(l1)
            first = True
        else:
            mod.append(l1.val)
        if type(l2) == int:
            mod.append(l2)
            second = True
        else:
            mod.append(l2.val)
        
        outInts.append(sum(mod))
        mod = []

        if first and second:
            return outInts
        elif first:
            return add(None, l2.next, outInts)
        elif second:
            return add(l1.next, None, outInts)
    return add(l1.next, l2.next, outInts)        
        


if __name__ == '__main__':
    L1 = ListNode(2,ListNode(4,3))
    L2 = ListNode(5,ListNode(6,4))
    print(addTwoNumbers(L1,L2))
    