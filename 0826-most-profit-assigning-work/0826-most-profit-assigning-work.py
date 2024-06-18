class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples
        jobs = list(zip(difficulty, profit))
        # Sort jobs by difficulty
        jobs.sort()
        # Sort workers by their ability
        worker.sort()

        max_profit = 0
        best_profit = 0
        job_index = 0

        # Iterate through each worker's ability
        for ability in worker:
            # Find the best job this worker can do
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            # Add the best profit this worker can earn to total profit
            max_profit += best_profit

        return max_profit