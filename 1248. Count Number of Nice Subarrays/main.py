class Solution:
    def numberOfSubarrays(self, nums, k):
        # Helper function to find the indices of all odd numbers
        def odd_indices(nums):
            return [i for i, num in enumerate(nums) if num % 2 != 0]

        odds = odd_indices(nums)
        n = len(odds)
        
        if n < k:
            return 0
        
        count = 0
        for i in range(n - k + 1):
            left = odds[i] - (odds[i - 1] if i > 0 else -1)
            right = (odds[i + k] if i + k < n else len(nums)) - odds[i + k - 1]
            count += left * right
        
        return count

# Example cases
solution = Solution()
print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
print(solution.numberOfSubarrays([2, 4, 6], 1))        # Output: 0
print(solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # Output: 16
