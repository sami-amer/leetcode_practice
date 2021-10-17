# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head # Set them all
        for _ in range(n): # Move fast to the nth node
            fast = fast.next
        if not fast: # if we already hit the end
            return head.next # return the head
        while fast.next: # otherwise iterate until we get to the end of fast
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # this skips the value
        return head # I have zero clue how this works

if __name__ == "__main__":
    input = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(Solution.removeNthFromEnd(None, input,2))