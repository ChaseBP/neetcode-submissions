# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        slow, fast = dummyNode, dummyNode
        #Move fast -> 'n' times
        for _ in range(n):
            if fast:
                fast = fast.next
        while fast.next:
            #Move slow -> once
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummyNode.next

