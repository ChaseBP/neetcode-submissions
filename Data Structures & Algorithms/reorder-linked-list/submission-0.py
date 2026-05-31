# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        DUMMY_NODE = ListNode()
        slow = head
        fast = head
        curr = DUMMY_NODE #For the start of the new list

        #Arrive at the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Store the second half of the list 
        Scurr = slow.next # Start of the second list [4,5,6]

        #End of first list -> points to None 
        slow.next = None

        #Reverse the second list
        Sprev = None
        while Scurr:
            temp = Scurr.next
            Scurr.next = Sprev
            Sprev = Scurr 
            Scurr = temp
        
        #Merge the lists together (head->First list start , Sprev -> head of the reversed list  )

        curr.next = head

        while head and Sprev:
            tmp1 = head.next
            head.next = Sprev
            tmp2 = Sprev.next 
            Sprev.next = tmp1 
            head = tmp1 
            Sprev = tmp2
        
        head = curr.next
        