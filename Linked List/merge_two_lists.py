# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Start with a dummy node and a tail
        dummy = ListNode()
        tail = dummy

        # Update the next pointer comparing both values from each list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next=list2
                list2 = list2.next
            tail = tail.next

        # when one list ends other can still exist so point the end of the tail
        # to the other list accordingly
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
