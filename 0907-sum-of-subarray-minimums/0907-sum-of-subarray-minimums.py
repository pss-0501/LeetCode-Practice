class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
    
        # Arrays to store the count of subarrays for which arr[i] is the minimum
        left = [0] * n
        right = [0] * n

        # Monotonic stack to find previous less element
        stack = []
        for i in range(n):
            # Calculate left[i]
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]

            left[i] = count
            stack.append((arr[i], count))

        stack = []
        for i in range(n - 1, -1, -1):
            # Calculate right[i]
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % mod

        return result