class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        
        # Count occurrences of each string in arr
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        
        # Collect distinct strings in order
        distinct = []
        for s in arr:
            if count[s] == 1:
                distinct.append(s)
        
        # Check if there are at least k distinct strings
        if k <= len(distinct):
            return distinct[k - 1]
        else:
            return ""