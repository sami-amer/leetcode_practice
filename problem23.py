# Definition for singly-linked list.
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        res = defaultdict(int)
        tracker = output = ListNode()
        for l in lists:
            traversal = l
            if traversal:
                while traversal.next:
                    res[traversal.val] += 1
                    traversal = traversal.next
                res[traversal.val] += 1
        print(res)
        for key in sorted(res.keys()):
            if res[key] == 0:
                continue
            for _ in range(res[key]):
                tracker.next = ListNode(key)
                tracker = tracker.next
        return output.next


        # tracker = output = ListNode()
        # while not l.count(None) == len(l):
        #     minimum = float('inf')
        #     for i,l in enumerate(lists):
        #         if not l:
        #             continue
        #         if l.val < minimum:
        #             minimum = l.val
        #             min_l = i
                
        #     tracker.next = ListNode(minimum)
        #     tracker = tracker.next if tracker.next else 0
        #     lists[min_l] = lists[min_l].next if lists[min_l] else None
            
        # return output.next
                    