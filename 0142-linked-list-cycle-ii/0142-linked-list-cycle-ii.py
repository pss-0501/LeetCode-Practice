class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BF
        
        if not head or not head.next:
            return None

        cycle = []
        curr = head
        while curr and curr.next:
            cycle.append(curr)
            if curr.next in cycle:
                return curr.next
            curr = curr.next
        return None

        #optiimise


        # if not head or not head.next:
        #     return None

        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         # Cycle detected, now find the start of the cycle
        #         slow = head
        #         while slow != fast:
        #             slow = slow.next
        #             fast = fast.next
        #         return slow  # Cycle start node

        # return None  # No cycle found
