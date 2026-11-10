# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # BRUTE FORCE APPROACH 
        # TIME AND SPACE = O(n)

        # temp = head
        # sett = set()

        # while temp is not None:
        #     if temp in sett:
        #         return True
        #     sett.add(temp)
        #     temp = temp.next
        # return False

        # OPTIMAL APPROACH
        # TIME = O(n)
        # SPACE = O(1)

        slow , fast = head , head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True
        return False