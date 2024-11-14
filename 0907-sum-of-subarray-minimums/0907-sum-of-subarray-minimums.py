class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = 0
        n = len(arr)

        for i in range(n + 1):
            # Process each element in the array
            while stack and (i == n or arr[stack[-1]] > arr[i]):
                j = stack.pop()
                left = j - (stack[-1] if stack else -1)
                right = i - j
                res += arr[j] * left * right
                res %= MOD  # Take modulo to prevent overflow
            stack.append(i)


        return res