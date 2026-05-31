# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = ListNode() #Start of the new list
        curr = newList #Pointer to the new list

        while list1 and list2: #while both lists are there
            #Compare values of lists
            if list1.val < list2.val:
                curr.next = list1 #link the smaller node
                list1 = list1.next #move the list pointer
            else:
                curr.next = list2 #list2 is smaller
                list2 = list2.next 
            #Move the current pointer
            curr = curr.next
        #If any list reaches end (list1 == None or list2 == None)

        if list1:
            curr.next = list1
        elif list2: 
            curr.next = list2

        return newList.next

        