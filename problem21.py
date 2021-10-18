# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        tracker = output = ListNode()
        while l1 or l2:
            if not l1:
                tracker.next = (ListNode(l2.val))
                tracker = tracker.next
                l2 = l2.next
                continue
            elif not l2:
                tracker.next = (ListNode(l1.val))
                tracker = tracker.next
                l1 = l1.next
                continue
            if l1.val < l2.val or l1.val == l2.val:
                tracker.next = (ListNode(l1.val))
                tracker = tracker.next
                l1 = l1.next
            else:
                tracker.next = (ListNode(l2.val))
                tracker = tracker.next
                l2 = l2.next
        return output.next


if __name__ == "__main__":
    l1 = ListNode(1,ListNode(2,ListNode(3)))
    l2 = ListNode(1,ListNode(3,ListNode(4)))
    print(Solution.mergeTwoLists(None,l1,l2).val)



