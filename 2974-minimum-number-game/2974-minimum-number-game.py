class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sorting the array to easily find the minimum element
        arr = []
        while nums:
            # Alice removes the minimum element
            alice_move = nums.pop(0)
            # Bob removes the minimum element
            bob_move = nums.pop(0)
            # Bob appends his removed element
            arr.append(bob_move)
            # Alice appends her removed element
            arr.append(alice_move)
        return arr
                
    