class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the ratings are in strictly increasing order
                    if rating[i] < rating[j] < rating[k]:
                        count += 1
                    # Check if the ratings are in strictly decreasing order
                    elif rating[i] > rating[j] > rating[k]:
                        count += 1
        
        return count