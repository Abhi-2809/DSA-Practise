# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # curr = head
        # val_set = set()
        # while curr:
        #     if curr in val_set:
        #         return True
        #     val_set.add(curr)
        #     print(curr)
        #     curr = curr.next
        
        # return False

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        
        return False

    




