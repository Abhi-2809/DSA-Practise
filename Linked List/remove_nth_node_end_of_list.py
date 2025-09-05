# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_length(self,head):

        count=0
        itr = head
        while itr:
            count+=1
            itr=itr.next
        
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        new_index = self.get_length(head) - n

        if new_index==0:
            head = head.next
            return head

        cnt=0
        itr = head
        while cnt!=new_index-1:
            cnt+=1
            itr=itr.next
        
        itr.next = itr.next.next

        return head




        
