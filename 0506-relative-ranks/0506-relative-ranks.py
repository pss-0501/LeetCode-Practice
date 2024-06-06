class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Step 1: Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Step 2: Create a dictionary to map scores to their ranks
        rank_dict = {}
        for rank, score_value in enumerate(sorted_scores):
            if rank == 0:
                rank_dict[score_value] = "Gold Medal"
            elif rank == 1:
                rank_dict[score_value] = "Silver Medal"
            elif rank == 2:
                rank_dict[score_value] = "Bronze Medal"
            else:
                rank_dict[score_value] = str(rank + 1)
        
        # Step 3: Generate the result array based on the original scores
        result = [rank_dict[score_value] for score_value in score]
        
        return result