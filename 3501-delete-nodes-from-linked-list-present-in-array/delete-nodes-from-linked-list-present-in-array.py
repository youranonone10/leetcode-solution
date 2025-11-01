# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        # Convert nums to a set for O(1) lookups
        remove_set = set(nums)
        
        # Create a dummy node to handle head removals easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val in remove_set:
                # Skip the node if it should be removed
                current.next = current.next.next
            else:
                # Move forward
                current = current.next
        
        return dummy.next
